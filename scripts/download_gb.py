import os
import sys
from Bio import Entrez

def download_by_gi(result_dir, gi):
    Entrez.email = "3066268521@qq.com"
    filename = gi+".gb"
    if not os.path.isfile(filename):
        print("Downloading..."+filename)
        net_handle = Entrez.efetch(db="nucleotide", id=gi, rettype="gb", retmode="text")
        out_handle = open(result_dir+'/identification/'+filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")

def download_by_accession_version(result_dir, accession_version):
    Entrez.email = "3066268521@qq.com"
    filename = accession_version+".gb"
    if not os.path.isfile(filename):
        print("Downloading..."+filename)
        net_handle = Entrez.efetch(db="nucleotide", id=accession_version, rettype="gb", retmode="text")
        out_handle = open(result_dir+'/identification/'+filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")

# def download_by_gi():
#     argv = sys.argv
#     gi = argv[1]
#     Entrez.email = "3066268521@qq.com"
#     filename = "gi_"+gi+".gb"
#     if not os.path.isfile(filename):
#         print("Downloading...")
#         net_handle = Entrez.efetch(db="nucleotide", id=gi, rettype="gb", retmode="text")
#         out_handle = open(filename, "w")
#         out_handle.write(net_handle.read())
#         out_handle.close()
#         net_handle.close()
#         print("Saved")

# if __name__ == "__main__":
#     download_by_gi()
