import subprocess


def prediction(input_file, result_dir):
    print("Begin Prodigal")
    print("input_file="+input_file)
    subprocess.run('mkdir '+result_dir+'/denovo/prodigal', shell=True, check=True)
    subprocess.run('prodigal -i ' + input_file + ' -a '+result_dir+'/denovo/prodigal/proteins.faa -o '+result_dir+'/denovo/prodigal/genes -d '+result_dir+'/denovo/prodigal/nucleotide_seq.fasta -s '+result_dir+'/denovo/prodigal/potential.stat', shell=True, check=True)
    print("End Prodigal")
