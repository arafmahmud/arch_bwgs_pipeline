import os 





class fastq_preproccessing:

    def __init__(self,input_folder, foldr, sample):
        self.input_folder = input_folder
        self.foldr = foldr
        self.sample = sample

    def merger_nextseq(self):
        mkdr = "mkdir {foldr}/{sample}".format(foldr = self.foldr, sample = self.sample)
        os.system(mkdr)
        mer = "rsync -av {input_folder}/{sample}_*/ {foldr}/{sample}".format(input_folder = self.input_folder, foldr = self.foldr, sample = self.sample)
        os.system(mer)
        unzip = "gzip -d {foldr}/{sample}/*.gz".format(foldr = self.foldr, sample = self.sample)
        os.system(unzip)
        cat1  = "cat {foldr}/{sample}/*_R1_001.fastq > {foldr}/{sample}/{sample}_R1.fastq".format(foldr = self.foldr, sample = self.sample)
        cat2 = "cat {foldr}/{sample}/*_R2_001.fastq > {foldr}/{sample}/{sample}_R2.fastq".format(foldr = self.foldr, sample = self.sample)
        os.system(cat1)
        os.system(cat2)
        os.system("rm -r {foldr}/{sample}/*_001.fastq".format(foldr = self.foldr, sample = self.sample))

    def merger_miseq(self):
        mkdr = "mkdir {foldr}/{sample}".format(foldr = self.foldr, sample = self.sample)
        os.system(mkdr)
        mer = "rsync -av {input_folder}/{sample}_* {foldr}/{sample}".format(input_folder = self.input_folder, foldr = self.foldr, sample = self.sample)
        os.system(mer)
        unzip = "gzip -d {foldr}/{sample}/*.gz".format(foldr = self.foldr, sample = self.sample)
        os.system(unzip)
        cat1  = "cat {foldr}/{sample}/*_R1_001.fastq > {foldr}/{sample}/{sample}_R1.fastq".format(foldr = self.foldr, sample = self.sample)
        cat2 = "cat {foldr}/{sample}/*_R2_001.fastq > {foldr}/{sample}/{sample}_R2.fastq".format(foldr = self.foldr, sample = self.sample)
        os.system(cat1)
        os.system(cat2)
        os.system("rm -r {foldr}/{sample}/*_001.fastq".format(foldr = self.foldr, sample = self.sample))
    

           
		




