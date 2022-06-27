import os 
import pandas as pd 
import concurrent.futures
import time
import subprocess


class Coverage_calculator:



	def __init__(self, foldr, sample):
		self.foldr = foldr
		self.sample = sample

    
	def coveragecalc(self):
		maping = "bwa mem -t 12 {foldr}/assembled_fasta/{sample}.fasta {foldr}/{sample}/*R1.fastq {foldr}/{sample}/*R2.fastq > {foldr}/{sample}/aln_map.sam".format(foldr = self.foldr, sample = self.sample)
		os.system(maping)
		samtobam = "samtools view -S -b {foldr}/{sample}/aln_map.sam > {foldr}/{sample}/aln.bam".format(foldr = self.foldr, sample = self.sample)
		os.system(samtobam)
		bamsort = "samtools sort {foldr}/{sample}/aln.bam --reference  {foldr}/assembled_fasta/{sample}.fasta > {foldr}/{sample}/aln_sort.bam".format(foldr = self.foldr, sample = self.sample)
		os.system(bamsort)
		coverdir = "mkdir {foldr}/coverage".format(foldr = self.foldr)
		os.system(coverdir)
		calculate_coverage = "samtools depth {foldr}/{sample}/aln_sort.bam".format(foldr = self.foldr, sample = self.sample) + "|  awk '" +"{"+ "sum+=$3" +"} END "+ "{" + '''print "{sample}, ",sum/NR'''.format(sample = self.sample) + "}'" +">"  + "{foldr}/coverage/{sample}.txt".format(sample = self.sample, foldr = self.foldr)
		subprocess.call(calculate_coverage, shell = "true")
		rm_files = "rm -r {foldr}/{sample}/*.bam {foldr}/{sample}/*.sam {foldr}/assembled_fasta/*amb {foldr}/assembled_fasta/*ann {foldr}/assembled_fasta/*bwt {foldr}/assembled_fasta/*pac {foldr}/assembled_fasta/*sa".format(foldr = self.foldr, sample = self.sample)
		os.system(rm_files)

	def indexmaker(self):
		ind = "bwa index -a bwtsw {foldr}/assembled_fasta/{sample}.fasta".format(foldr = self.foldr, sample = self.sample)
		os.system(ind)




