import os
import sys
from BCBio import GFF
from Bio import SeqIO
import subprocess

class Genbank2gff3:

    in_file = ''
    out_file = ''
    result_dir = ''

    def __init__(self, file_name, result_dir):
        if ".gb" == file_name[-3:]:
            file_name = file_name[:-3]
        elif ".genbank" == file_name[-8:]:
            file_name = file_name[:-8]
        self.in_file = file_name + ".gb"
        self.out_file = file_name + ".gff"
        self.result_dir = result_dir
    
    def genbank2gff3_by_bioperl(self):
        print("begin genbank2gff3_by_bioperl")
        subprocess.run('bp_genbank2gff3 '+self.result_dir+'/identification/'+self.in_file+' --outdir '+self.result_dir+'/identification/ --split', shell=True, check=True)
        result_file_name = self.in_file + ".gff"
        if os.path.exists(self.result_dir+'/identification/'+result_file_name):
            subprocess.run('mv '+self.result_dir+'/identification/'+result_file_name+" "+self.result_dir+'/identification/'+self.out_file, shell=True, check=True)
        elif os.path.exists(self.result_dir+'/identification/'+result_file_name.split('/')[-1]):
            subprocess.run('mv '+self.result_dir+'/identification/'+result_file_name.split('/')[-1]+" "+self.result_dir+'/identification/'+self.out_file, shell=True, check=True)
        print("end genbank2gff3_by_bioperl")

    def genbank2gff3_by_bcbio(self):
        print("begin genbank2gff3_by_bcbio")
        in_handle = open(self.result_dir+'/identification/'+self.in_file)
        out_handle = open(self.result_dir+'/identification/'+self.out_file,"w")
        GFF.write(SeqIO.parse(in_handle,'genbank'), out_handle)
        in_handle.close()
        out_handle.close()
        print("end genbank2gff3_by_bcbio")

# def main():
#     argv = sys.argv
#     input = argv[1]
#     transform = Genbank2gff3(input)
#     # transform.genbank2gff3_by_bcbio()
#     transform.genbank2gff3_by_bioperl()

# if __name__ == "__main__":
#     main()
