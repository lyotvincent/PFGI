import os
import sys
# from bioconvert import fasta2fastq
from Bio import SeqIO

# def fasta_to_fastq(input_fasta, result_dir):
#     print('begin fasta2fastq')
#     # argv = sys.argv
#     # file_name = argv[1]
#     file_name = input_fasta
#     print(file_name)
#     if ".fa" == file_name[-3:]:
#         # transformer = fasta2fastq.Fasta2Fastq(file_name, file_name[:-3]+".fastq")
#         transformer = fasta2fastq.FASTA2FASTQ(file_name, result_dir+"/identification/assembly_result.fastq")
#         transformer._method_pysam()
#     elif ".fasta" == file_name[-6:]:
#         # transformer = fasta2fastq.Fasta2Fastq(file_name, file_name[:-6]+".fastq")
#         transformer = fasta2fastq.FASTA2FASTQ(file_name, result_dir+"/identification/assembly_result.fastq")
#         transformer._method_pysam()
#     print('end fasta2fastq')

# if __name__ == "__main__":
#     fasta_to_fastq()

def fasta_to_fastq_by_biopython(input_fasta, result_dir):
    print('begin fasta2fastq')
    fa_path = input_fasta
    fq_path = result_dir+"/identification/assembly_result.fastq"

    with open(fa_path, "r") as fasta, open(fq_path, "w") as fastq:
        for record in SeqIO.parse(fasta, "fasta"):
            record.letter_annotations["phred_quality"] = [40] * len(record)
            SeqIO.write(record, fastq, "fastq")
    print('end fasta2fastq')