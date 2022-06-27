
from .downstream import Downstream
from .preprocessing import fastq_preproccessing
from .assembly import Assembly_pipeline
from .coverage import Coverage_calculator
import os
import argparse
import pandas as pd
import concurrent.futures

parser = argparse.ArgumentParser(prog="arch_bwgs_pipeline.py", formatter_class=argparse.RawTextHelpFormatter, description="""
arch_BWGS_pipeline is an automated pipeline for Microbial Sequence assembly\n""",epilog="""
    Examples:
    python3 arch_bwgs_pipeline.py -i input_folder -o output_folder -s sample_sheet.csv""")


parser.add_argument("-i", "--input", type=str, default="", required=True, help="input folder directory")
parser.add_argument("-o", "--output", type=str, default="", required=True, help="output folder directory")
parser.add_argument("-s", "--sample_sheet", type=str, default="", required=True, help="sample names is a csv file")
parser.add_argument("-tf1", "--trim_front1", type=str, default="15", required=False, help="trim front1  int=(default 15) ")
parser.add_argument("-tf2", "--trim_front2", type=str, default="15", required=False, help="trim front2  int=(default 15) ")
parser.add_argument("-tt1", "--trim_tail1", type=str, default="3", required=False, help="trim tail1 int=(default 3) ")
parser.add_argument("-tt2", "--trim_tail2", type=str, default="3", required=False, help="trim tail2 int=(default 3) ")
parser.add_argument("-system", "--sequencer", type=str, default="nextseq", required=False, help="Sequencing system (miseq AND nextseq IS SUPPORTED)(default = nextseq)")
parser.add_argument("-amr", "--amr", type=str, default="y", required=False, help="Generates AMR gene report(NO POINT MUTATION DATA IS GENERATED)(y or n) (default y)")
parser.add_argument("-vir", "--virulence", type=str, default="y", required=False, help="Generates virulence gene report (y or n) (default y)")
parser.add_argument("-t", "--threads", type=str, default="4", required=False, help="number of threads int= (default 4)")
parser.add_argument("-p", "--parallel", type=str, default="1", required=False, help="paralellization int= (default 1)")
parser.add_argument("-min", "--minimum_contig_length", type=str, default="100", required=False, help="minimum contig length (default 100)")


args = parser.parse_args()


df = pd.read_csv(args.sample_sheet, names=["ids"])
samples = list(df.ids)
print(samples)
os.system("mkdir {}".format(args.output))

os.system("mkdir {}/coverage {}/virulence_report {}/amr_report".format(args.output,args.output,args.output))


def preprocessor(input, output, sequencer, sample):
    preprocess = fastq_preproccessing(input, output, sample)
    if sequencer == "nextseq":
        preprocess.merger_nextseq()
    if sequencer == "miseq":
        preprocess.merger_miseq()
    else:
        print("Select a valid arguement")
        quit()

def assembler_pipeline(output, sample, trim_front1,trim_front2, trim_tail1, trim_tail2, threads, minimum_contig_length):
    pipeline = Assembly_pipeline(output, sample, trim_front1, trim_front2, trim_tail1, trim_tail2, threads, minimum_contig_length)
    pipeline.mkdr()
    pipeline.fastqc()
    pipeline.trimmer_fastp()
    pipeline.assembly()
    pipeline.annotate()
    pipeline.assessment()
    pipeline.fasta_collector()
    pipeline.short_seq_removal()

def find_coverage(output,sample):
    cov = Coverage_calculator(output, sample)
    cov.indexmaker()
    cov.coveragecalc()

def amr_finder(output, sample):
    down = Downstream(output,sample)
    down.amr_gene_finder()

def vir_finder(output, sample):
    down = Downstream(output,sample)
    down.virulence_gene_finder()


def main():
    
    parallelization_count = int(args.parallel)
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = parallelization_count) as executor:
        run_preprocessor = [executor.submit(preprocessor,args.input, args.output, args.sequencer, sample_id) for sample_id in samples]

    with concurrent.futures.ThreadPoolExecutor(max_workers = parallelization_count) as executor:
        run_assembler_pipeline = [executor.submit(assembler_pipeline,args.output, sample, args.trim_front1, args.trim_front2, args.trim_tail1, args.trim_tail2, args.threads, args.minimum_contig_length) for sample in samples]

    with concurrent.futures.ThreadPoolExecutor(max_workers = parallelization_count) as executor:
        run_find_coverage = [executor.submit(find_coverage, args.output, sample) for sample in samples]

    if args.amr == "y":
        with concurrent.futures.ThreadPoolExecutor(max_workers = parallelization_count) as executor:
            run_amr_find = [executor.submit(amr_finder, args.output, sample) for sample in samples]
    else:
        pass

    if args.virulence == "y":
        with concurrent.futures.ThreadPoolExecutor(max_workers = parallelization_count) as executor:
            run_vir_finder = [executor.submit(vir_finder, args.output, sample) for sample in samples]
    else:
        pass


if __name__=="__main__":
    main()
