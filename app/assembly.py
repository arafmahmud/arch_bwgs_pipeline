import os 


class Assembly_pipeline:

	def __init__(self, foldr, sample, trim_front1, trim_front2,trim_tail1,trim_tail2, threads, minimum_contig_length):
		self.foldr = foldr
		self.sample = sample
		self.threads = threads
		self.trim_front1 = trim_front1
		self.trim_front2 = trim_front2
		self.trim_tail1 = trim_tail1
		self.trim_tail2 = trim_tail2
		self.minimum_contig_length = minimum_contig_length
	def mkdr(self):
		mkdr = "mkdir {foldr}/{sample}/fastqc_report {foldr}/{sample}/trimmed {foldr}/assembled_fasta".format(foldr = self.foldr, sample = self.sample)
		os.system(mkdr)

	def fastqc(self):
		print("🄶🄴🄽🄴🅁🄰🅃🄸🄽🄶 🅀🄲 🅁🄴🄿🄾🅁🅃....")		
		fqc = "fastqc -o {foldr}/{sample}/fastqc_report -t {threads} {foldr}/{sample}/{sample}_R*.fastq".format(threads = self.threads, foldr = self.foldr, sample = self.sample)
		os.system(fqc)
		
	
	def trimmer_fastp(self):
		print("🄿🄴🅁🄵🄾🅁🄼🄸🄽🄶 🅀🅄🄰🄻🄸🅃🅈 🅃🅁🄸🄼🄼🄸🄽🄶....")
		trim = 	"fastp -i {foldr}/{sample}/{sample}_R1.fastq -I {foldr}/{sample}/{sample}_R2.fastq \
			-o {foldr}/{sample}/trimmed/{sample}_R1.fastq -O {foldr}/{sample}/trimmed/{sample}_R2.fastq \
			--trim_front1 {trim_front1} trim_front2 {trim_front2} --trim_poly_g --trim_tail1 {trim_tail1} \
			 --trim_tail2 {trim_tail2}  --thread {threads} ".format(trim_front1 = self.trim_front1,trim_front2 = self.trim_front2,trim_tail1 = self.trim_tail1,trim_tail2 = self.trim_tail2, threads = self.threads, foldr = self.foldr, sample = self.sample)
		os.system(trim)

	def assembly(self):
		print("🄰🅂🅂🄴🄼🄱🄻🅈")
		assemble = "spades -k 21,33,55,77,87,99,111,119,127 --careful --pe1-1 {foldr}/{sample}/trimmed/{sample}_R1.fastq \
				 --pe1-2 {foldr}/{sample}/trimmed/{sample}_R2.fastq -o {foldr}/{sample}/assembly -t {threads}".format(threads = self.threads,foldr = self.foldr, sample = self.sample)
		os.system(assemble)

	def annotate(self):
		print("🄰🄽🄽🄾🅃🄰🅃🄸🄽🄶")
		annotation = "prokka --outdir {foldr}/{sample}/prokka --cpus 12 --prefix {sample} {foldr}/{sample}/assembly/contigs.fasta".format(foldr = self.foldr, sample = self.sample)
		os.system(annotation)

	def assessment(self):
		print("🄰🅂🅂🄴🄼🄱🄻🅈 🄰🅂🅂🄴🅂🅂🄼🄴🄽🅃......")
		assess = "quast.py -o {foldr}/{sample}/quast_results  \
			 -t {threads} -1 {foldr}/{sample}/trimmed/*_R1.fastq -2 {foldr}/{sample}/trimmed/*_R2.fastq  -g {foldr}/{sample}/prokka/*.gff\
			 --gene-thresholds 1,1000 {foldr}/{sample}/assembly/contigs.fasta --glimmer".format(threads = self.threads, foldr = self.foldr, sample = self.sample)
		os.system(assess)

	def fasta_collector(self):
		cp  = "cp {foldr}/{sample}/assembly/contigs.fasta {foldr}/assembled_fasta/{sample}.fasta".format(foldr = self.foldr, sample = self.sample)
		os.system(cp)

	def short_seq_removal(self):
		seqtk = "seqtk subseq -L {minimum_contig_length} {foldr}/assembled_fasta/{sample}.fasta > {foldr}/assembled_fasta/{sample}.fasta".format(foldr = self.foldr, sample = self.sample, minimum_contig_length = self.minimum_contig_length)
		os.system(seqtk)
	
	