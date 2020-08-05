import subprocess


def annotation(input_file, result_dir, conf, closest_accession_version):
    print("Begin Prokka")
    print("input_file="+input_file)
    prokka_conf = conf['annotation']['prokka']
    command_line = 'prokka --outdir '+result_dir+'/prokka_annotation '
    if prokka_conf['--addgenes'] != None:
        command_line += '--addgenes '
    if prokka_conf['--addmrna'] != None:
        command_line += '--addmrna '
    command_line += '--proteins '+result_dir+'/identification/'+closest_accession_version+'.fasta '
    if prokka_conf['--evalue'] != None:
        command_line += '--evalue '+str(prokka_conf['--evalue'])+' '
    if prokka_conf['--coverage'] != None:
        command_line += '--coverage '+str(prokka_conf['--coverage'])+' '
    if prokka_conf['--cpus'] != None:
        command_line += '--cpus '+str(prokka_conf['--cpus'])+' '
    if prokka_conf['--mincontiglen'] != None:
        command_line += '--mincontiglen '+str(prokka_conf['--mincontiglen'])+' '
    if prokka_conf['--rfam'] != None:
        command_line += '--rfam '
    if prokka_conf['--norrna'] != None:
        command_line += '--norrna '
    if prokka_conf['--notrna'] != None:
        command_line += '--notrna '
    if prokka_conf['--rnammer'] != None:
        command_line += '--rnammer '
    command_line += input_file
    subprocess.run(command_line, shell=True, check=True)
    print("End Prokka")
