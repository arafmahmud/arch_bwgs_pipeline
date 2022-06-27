import os

class Downstream:

    def __init__(self, foldr, sample):
        self.foldr = foldr
        self.sample = sample
    
    def amr_gene_finder(self):
        amr = "abricate {foldr}/assembled_fasta/{sample}.fasta > {foldr}/amr_report/{sample}.txt".format(foldr = self.foldr, sample = self.sample)
        print(amr)
        os.system(amr)

    def virulence_gene_finder(self):
        vir = "abricate --db vfdb {foldr}/assembled_fasta/{sample}.fasta > {foldr}/virulence_report/{sample}.txt".format(foldr = self.foldr, sample = self.sample)
        print(vir)
        os.system(vir)

