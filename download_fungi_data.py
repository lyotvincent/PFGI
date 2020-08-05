import subprocess
import time

class Downloader:


    def __init__(self):
        super().__init__()


    def download_assembly_summary(self):
        subprocess.run('wget -c -T 10 -t 0 ftp://ftp.ncbi.nlm.nih.gov/genomes/genbank/fungi/assembly_summary.txt', shell=True, check=True)


    def download_fna(self):
        print('downloading fna')
        assembly_summary = open('assembly_summary.txt', 'r', encoding = 'UTF-8')
        assembly_summary_lines = assembly_summary.readlines()
        assembly_summary.close()

        i = 0
        for assembly_summary_line in assembly_summary_lines:
            if assembly_summary_line.startswith('#'): continue
            if assembly_summary_line.strip().split('\t')[11] != 'Complete Genome' and assembly_summary_line.strip().split('\t')[11] != 'Chromosome': continue
            ftp_path = assembly_summary_line.strip().split('\t')[19]
            fna_ftp_path = ftp_path + '/' + ftp_path.split('/')[-1] + '_genomic.fna.gz'
            try:
                time.sleep(5)
                subprocess.run('wget -c -T 10 --tries=0 --retry-connrefused %s' % fna_ftp_path, shell=True, check=True)
            except:
                fil = open('undownloadedseq.txt', 'a+')
                fil.write(fna_ftp_path+"\n")
                fil.close()

            # i += 1
            # if i==10: break

    def decompressed(self):
        subprocess.run('gunzip -f ./*.fna.gz', shell=True, check=True)
    
    def cat_in_one(self):
        subprocess.run('cat ./*.fna > fungi_sequences.fasta', shell=True, check=True)
    
    def makeblastdb(self):
        subprocess.run('makeblastdb -in fungi_sequences.fasta -dbtype nucl -parse_seqids -out fungi_db', shell=True, check=True)

# CARD
# wget -c --no-check-certificate -T 10 --tries=0 --retry-connrefused -O card-data.tar.bz2 https://card.mcmaster.ca/latest/data
# wget -c --no-check-certificate -T 10 --tries=0 --retry-connrefused -O card-prevalence.tar.bz2 https://card.mcmaster.ca/latest/variants/

if __name__ == "__main__":
    downloader = Downloader()
    downloader.download_assembly_summary()
    downloader.download_fna()
    downloader.decompressed()
    downloader.cat_in_one()
    downloader.makeblastdb()
