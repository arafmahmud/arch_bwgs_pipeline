# arch_bwgs_pipeline
Bacterial Whole Genome Analysis Pipeline

# Installation

Create a conda environment:
```
conda create --name arch_bwgs_pipeline
conda activate arch_bwgs_pipeline`
```
Install dependencies:
```
 pip3 install pandas
 conda install -y -c conda-forge -c bioconda -c defaults prokka 
 prokka --setupdb
 conda install -y -c bioconda spades
 conda install -y -c bioconda abricate
 conda install -y -c bioconda fastqc
 conda install -y -c bioconda fastp
 conda install -y -c bioconda quast
 conda install -y -c bioconda seqtk
 conda install -y -c bioconda bwa
 conda install -y -c bioconda samtools`
 ```
 # Sample Sheet format(sample_sheet.csv)
 
 ```
 #strain IDs from sample sheet
 sample1
 sample2
 sample3
 ```
 
 # Run pipeline:
 
``` 
arch_bwgs_pipeline -h
usage: arch_bwgs_pipeline.py [-h] -i INPUT -o OUTPUT -s SAMPLE_SHEET
                             [-tf1 TRIM_FRONT1] [-tf2 TRIM_FRONT2]
                             [-tt1 TRIM_TAIL1] [-tt2 TRIM_TAIL2]
                             [-system SEQUENCER] [-amr AMR] [-vir VIRULENCE]
                             [-t THREADS] [-p PARALLEL]
                             [-min MINIMUM_CONTIG_LENGTH]

arch_BWGS_pipeline is an automated pipeline for Microbial Sequence assembly

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input folder directory
  -o OUTPUT, --output OUTPUT
                        output folder directory
  -s SAMPLE_SHEET, --sample_sheet SAMPLE_SHEET
                        sample names is a csv file
  -tf1 TRIM_FRONT1, --trim_front1 TRIM_FRONT1
                        trim front1  int=(default 15) 
  -tf2 TRIM_FRONT2, --trim_front2 TRIM_FRONT2
                        trim front2  int=(default 15) 
  -tt1 TRIM_TAIL1, --trim_tail1 TRIM_TAIL1
                        trim tail1 int=(default 3) 
  -tt2 TRIM_TAIL2, --trim_tail2 TRIM_TAIL2
                        trim tail2 int=(default 3) 
  -system SEQUENCER, --sequencer SEQUENCER
                        Sequencing system (miseq AND nextseq IS SUPPORTED)(default = nextseq)
  -amr AMR, --amr AMR   Generates AMR gene report(NO POINT MUTATION DATA IS GENERATED)(y or n) (default y)
  -vir VIRULENCE, --virulence VIRULENCE
                        Generates virulence gene report (y or n) (default y)
  -t THREADS, --threads THREADS
                        number of threads int= (default 4)
  -p PARALLEL, --parallel PARALLEL
                        paralellization int= (default 1)
  -min MINIMUM_CONTIG_LENGTH, --minimum_contig_length MINIMUM_CONTIG_LENGTH
                        minimum contig length (default 100)

    Examples:
    arch_bwgs_pipeline -i input_folder -o output_folder -s sample_sheet.csv
    
