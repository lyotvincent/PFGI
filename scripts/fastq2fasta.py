import os
import sys
from Bio import SeqIO

def fastq2fasta(input_fastq, result_dir):
    print('convert '+str(input_fastq)+' to fasta')
    SeqIO.convert(input_fastq, "fastq", result_dir+"/input.fasta", "fasta")

# def fastq2fasta():
#     argv = sys.argv
#     file = argv[1]
#     SeqIO.convert(file+".fastq", "fastq", file+".fasta", "fasta")

# if __name__ == "__main__":
#     fastq2fasta()