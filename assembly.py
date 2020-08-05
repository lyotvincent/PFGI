import subprocess
import os

class Assembly:

    result_dir = None
    conf = None
    input_file = None
    input_file_1 = None
    input_file_2 = None
    input_file_12 = None

    def __init__(self, result_dir, conf, input_file=None, input_file_1=None, input_file_2=None, input_file_12=None):
        self.result_dir = result_dir
        self.conf = conf
        self.input_file = input_file
        self.input_file_1 = input_file_1
        self.input_file_2 = input_file_2
        self.input_file_12 = input_file_12

    def megahit_single(self):
        print("begin megahit_single_end")
        megahit_conf = self.conf['megahit']
        command_line = '%s/external_tools/MEGAHIT/megahit ' % os.path.dirname(os.path.realpath(__file__))
        if megahit_conf['--min-count'] != None:
            command_line += '--min-count '+str(megahit_conf['--min-count'])+' '
        if megahit_conf['--k-list'] != None:
            command_line += '--k-list '+str(megahit_conf['--k-list'])+' '
        if megahit_conf['--no-mercy'] != None:
            command_line += '--no-mercy '
        if megahit_conf['--bubble-level'] != None:
            command_line += '--bubble-level '+str(megahit_conf['--bubble-level'])+' '
        if megahit_conf['--merge-level'] != None:
            command_line += '--merge-level '+str(megahit_conf['--merge-level'])+' '
        if megahit_conf['--prune-level'] != None:
            command_line += '--prune-level '+str(megahit_conf['--prune-level'])+' '
        if megahit_conf['--prune-depth'] != None:
            command_line += '--prune-depth '+str(megahit_conf['--prune-depth'])+' '
        if megahit_conf['--low-local-ratio'] != None:
            command_line += '--low-local-ratio '+str(megahit_conf['--low-local-ratio'])+' '
        if megahit_conf['--max-tip-len'] != None:
            command_line += '--max-tip-len '+str(megahit_conf['--max-tip-len'])+' '
        if megahit_conf['--no-local'] != None:
            command_line += '--no-local '
        if megahit_conf['--kmin-1pass'] != None:
            command_line += '--kmin-1pass '
        if megahit_conf['-m'] != None:
            command_line += '-m '+str(megahit_conf['-m'])+' '
        if megahit_conf['--mem-flag'] != None:
            command_line += '--mem-flag '+str(megahit_conf['--mem-flag'])+' '
        if megahit_conf['-t'] != None:
            command_line += '-t '+str(megahit_conf['-t'])+' '
        if megahit_conf['--no-hw-accel'] != None:
            command_line += '--no-hw-accel '
        if megahit_conf['--min-contig-len'] != None:
            command_line += '--min-contig-len '+str(megahit_conf['--min-contig-len'])+' '
        command_line += '-r '+self.input_file+' -o '+self.result_dir+'/megahit_out'
        subprocess.run(command_line, shell=True, check=True)
        print("end megahit_single_end")
    
    def megahit_paired(self):
        print("begin megahit_paired_end")
        megahit_conf = self.conf['megahit']
        command_line = '%s/external_tools/MEGAHIT/megahit ' % os.path.dirname(os.path.realpath(__file__))
        if megahit_conf['--min-count'] != None:
            command_line += '--min-count '+str(megahit_conf['--min-count'])+' '
        if megahit_conf['--k-list'] != None:
            command_line += '--k-list '+str(megahit_conf['--k-list'])+' '
        if megahit_conf['--no-mercy'] != None:
            command_line += '--no-mercy '
        if megahit_conf['--bubble-level'] != None:
            command_line += '--bubble-level '+str(megahit_conf['--bubble-level'])+' '
        if megahit_conf['--merge-level'] != None:
            command_line += '--merge-level '+str(megahit_conf['--merge-level'])+' '
        if megahit_conf['--prune-level'] != None:
            command_line += '--prune-level '+str(megahit_conf['--prune-level'])+' '
        if megahit_conf['--prune-depth'] != None:
            command_line += '--prune-depth '+str(megahit_conf['--prune-depth'])+' '
        if megahit_conf['--low-local-ratio'] != None:
            command_line += '--low-local-ratio '+str(megahit_conf['--low-local-ratio'])+' '
        if megahit_conf['--max-tip-len'] != None:
            command_line += '--max-tip-len '+str(megahit_conf['--max-tip-len'])+' '
        if megahit_conf['--no-local'] != None:
            command_line += '--no-local '
        if megahit_conf['--kmin-1pass'] != None:
            command_line += '--kmin-1pass '
        if megahit_conf['-m'] != None:
            command_line += '-m '+str(megahit_conf['-m'])+' '
        if megahit_conf['--mem-flag'] != None:
            command_line += '--mem-flag '+str(megahit_conf['--mem-flag'])+' '
        if megahit_conf['-t'] != None:
            command_line += '-t '+str(megahit_conf['-t'])+' '
        if megahit_conf['--no-hw-accel'] != None:
            command_line += '--no-hw-accel '
        if megahit_conf['--min-contig-len'] != None:
            command_line += '--min-contig-len '+str(megahit_conf['--min-contig-len'])+' '
        command_line += '-1 '+self.input_file_1+' -2 '+self.input_file_2+' -o '+self.result_dir+'/megahit_out'
        subprocess.run(command_line, shell=True, check=True)
        print("end megahit_paired_end")

    def megahit_interleaved(self):
        print("begin megahit_interleaved")
        megahit_conf = self.conf['megahit']
        command_line = 'megahit '
        if megahit_conf['--min-count'] != None:
            command_line += '--min-count '+str(megahit_conf['--min-count'])+' '
        if megahit_conf['--k-list'] != None:
            command_line += '--k-list '+str(megahit_conf['--k-list'])+' '
        if megahit_conf['--no-mercy'] != None:
            command_line += '--no-mercy '
        if megahit_conf['--bubble-level'] != None:
            command_line += '--bubble-level '+str(megahit_conf['--bubble-level'])+' '
        if megahit_conf['--merge-level'] != None:
            command_line += '--merge-level '+str(megahit_conf['--merge-level'])+' '
        if megahit_conf['--prune-level'] != None:
            command_line += '--prune-level '+str(megahit_conf['--prune-level'])+' '
        if megahit_conf['--prune-depth'] != None:
            command_line += '--prune-depth '+str(megahit_conf['--prune-depth'])+' '
        if megahit_conf['--low-local-ratio'] != None:
            command_line += '--low-local-ratio '+str(megahit_conf['--low-local-ratio'])+' '
        if megahit_conf['--max-tip-len'] != None:
            command_line += '--max-tip-len '+str(megahit_conf['--max-tip-len'])+' '
        if megahit_conf['--no-local'] != None:
            command_line += '--no-local '
        if megahit_conf['--kmin-1pass'] != None:
            command_line += '--kmin-1pass '
        if megahit_conf['-m'] != None:
            command_line += '-m '+str(megahit_conf['-m'])+' '
        if megahit_conf['--mem-flag'] != None:
            command_line += '--mem-flag '+str(megahit_conf['--mem-flag'])+' '
        if megahit_conf['-t'] != None:
            command_line += '-t '+str(megahit_conf['-t'])+' '
        if megahit_conf['--no-hw-accel'] != None:
            command_line += '--no-hw-accel '
        if megahit_conf['--min-contig-len'] != None:
            command_line += '--min-contig-len '+str(megahit_conf['--min-contig-len'])+' '
        command_line += '-12 '+self.input_file_12+' -o '+self.result_dir+'/megahit_out'
        subprocess.run(command_line, shell=True, check=True)
        print("end megahit_interleaved")

    def spades_single(self):
        print("begin spades_single_end")
        spades_conf = self.conf['spades']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/SPAdes/bin/spades.py -s '+self.input_file+' '
        if spades_conf['--iontorrent'] != None:
            command_line += '--iontorrent '
        if spades_conf['-t'] != None:
            command_line += '-t '+str(spades_conf['-t'])+' '
        if spades_conf['-m'] != None:
            command_line += '-m '+str(spades_conf['-m'])+' '
        if spades_conf['-k'] != None:
            command_line += '-k '+str(spades_conf['-k'])+' '
        if spades_conf['--cov-cutoff'] != None:
            command_line += '--cov-cutoff '+str(spades_conf['--cov-cutoff'])+' '
        if spades_conf['--phred-offset'] != None:
            command_line += '--phred-offset '+str(spades_conf['--phred-offset'])+' '
        command_line += '-o '+self.result_dir+'/spades_out/'
        subprocess.run(command_line, shell=True, check=True)
        print("end spades_single_end")
    
    def spades_paired(self):
        print("begin spades_paired_end")
        spades_conf = self.conf['spades']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/SPAdes/bin/spades.py -1 '+self.input_file_1+' -2 '+self.input_file_2+' '
        if spades_conf['--iontorrent'] != None:
            command_line += '--iontorrent '
        if spades_conf['-t'] != None:
            command_line += '-t '+str(spades_conf['-t'])+' '
        if spades_conf['-m'] != None:
            command_line += '-m '+str(spades_conf['-m'])+' '
        if spades_conf['-k'] != None:
            command_line += '-k '+str(spades_conf['-k'])+' '
        if spades_conf['--cov-cutoff'] != None:
            command_line += '--cov-cutoff '+str(spades_conf['--cov-cutoff'])+' '
        if spades_conf['--phred-offset'] != None:
            command_line += '--phred-offset '+str(spades_conf['--phred-offset'])+' '
        command_line = '-o '+self.result_dir+'/spades_out/'
        subprocess.run(command_line, shell=True, check=True)
        print("end spades_paired_end")
    
    def spades_interlaced(self):
        print("begin spades_interlaced")
        spades_conf = self.conf['spades']
        command_line = 'spades.py -12 '+self.input_file_12+' '
        if spades_conf['--iontorrent'] != None:
            command_line += '--iontorrent '
        if spades_conf['-t'] != None:
            command_line += '-t '+str(spades_conf['-t'])+' '
        if spades_conf['-m'] != None:
            command_line += '-m '+str(spades_conf['-m'])+' '
        if spades_conf['-k'] != None:
            command_line += '-k '+str(spades_conf['-k'])+' '
        if spades_conf['--cov-cutoff'] != None:
            command_line += '--cov-cutoff '+str(spades_conf['--cov-cutoff'])+' '
        if spades_conf['--phred-offset'] != None:
            command_line += '--phred-offset '+str(spades_conf['--phred-offset'])+' '
        command_line += '-o '+self.result_dir+'/spades_out/'
        subprocess.run(command_line, shell=True, check=True)
        print("end spades_interlaced")
    
    def spades_3gs(self):
        print("begin spades_single_end")
        spades_conf = self.conf['spades']
        if spades_conf['--pacbio'] != None:
            command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/SPAdes/bin/spades.py --pacbio '+self.input_file+' '
        elif spades_conf['--nanopore'] != None:
            command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/SPAdes/bin/spades.py --nanopore '+self.input_file+' '
        else:
            print('please choose pacbio or nanopore in conf.json. use pacbio by default.')
            command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/SPAdes/bin/spades.py --pacbio '+self.input_file+' '
        if spades_conf['-t'] != None:
            command_line += '-t '+str(spades_conf['-t'])+' '
        if spades_conf['-m'] != None:
            command_line += '-m '+str(spades_conf['-m'])+' '
        if spades_conf['-k'] != None:
            command_line += '-k '+str(spades_conf['-k'])+' '
        if spades_conf['--cov-cutoff'] != None:
            command_line += '--cov-cutoff '+str(spades_conf['--cov-cutoff'])+' '
        if spades_conf['--phred-offset'] != None:
            command_line += '--phred-offset '+str(spades_conf['--phred-offset'])+' '
        command_line += '-o '+self.result_dir+'/spades_out/'
        subprocess.run(command_line, shell=True, check=True)
        print("end spades_single_end")

    def velvet_single(self):
        print('begin velvet_single_end')
        velveth_conf = self.conf['velvet']['velveth']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velveth '+self.result_dir+'/velvet_output/ '
        if velveth_conf['hash_length'] != None:
            command_line += str(velveth_conf['hash_length'])+' -fastq '
        else:
            command_line += "31 -fastq "
        if velveth_conf['-short'] != None:
            command_line += "-short "
        elif velveth_conf['-short2'] != None:
            command_line += '-short2 '
        elif velveth_conf['-long'] != None:
            command_line += '-long'
        else:
            command_line += "-short "
        command_line += self.input_file
        subprocess.run(command_line, shell=True, check=True)
        
        velvetg_conf = self.conf['velvet']['velvetg']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velvetg '+self.result_dir+'/velvet_output/ '
        if velvetg_conf['-cov_cutoff'] != None:
            command_line += '-cov_cutoff '+str(velvetg_conf['-cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-read_trkg'] != None:
            command_line += '-read_trkg '+str(velvetg_conf['-read_trkg'])+' '
        if velvetg_conf['-min_contig_lgth'] != None:
            command_line += '-min_contig_lgth '+str(velvetg_conf['-min_contig_lgth'])+' '
        if velvetg_conf['-amos_file'] != None:
            command_line += '-amos_file '+str(velvetg_conf['-amos_file'])+' '
        if velvetg_conf['-exp_cov'] != None:
            command_line += '-exp_cov '+str(velvetg_conf['-exp_cov'])+' '
        if velvetg_conf['-long_cov_cutoff'] != None:
            command_line += '-long_cov_cutoff '+str(velvetg_conf['-long_cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-ins_length_long'] != None:
            command_line += '-ins_length_long '+str(velvetg_conf['-ins_length_long'])+' '
        if velvetg_conf['-ins_length*_sd'] != None:
            command_line += '-ins_length*_sd '+str(velvetg_conf['-ins_length*_sd'])+' '
        if velvetg_conf['-scaffolding'] != None:
            command_line += '-scaffolding '+str(velvetg_conf['-scaffolding'])+' '
        if velvetg_conf['-max_branch_length'] != None:
            command_line += '-max_branch_length '+str(velvetg_conf['-max_branch_length'])+' '
        if velvetg_conf['-max_divergence'] != None:
            command_line += '-max_divergence '+str(velvetg_conf['-max_divergence'])+' '
        if velvetg_conf['-max_gap_count'] != None:
            command_line += '-max_gap_count '+str(velvetg_conf['-max_gap_count'])+' '
        if velvetg_conf['-min_pair_count'] != None:
            command_line += '-min_pair_count '+str(velvetg_conf['-min_pair_count'])+' '
        if velvetg_conf['-max_coverage'] != None:
            command_line += '-max_coverage '+str(velvetg_conf['-max_coverage'])+' '
        if velvetg_conf['-coverage_mask'] != None:
            command_line += '-coverage_mask '+str(velvetg_conf['-coverage_mask'])+' '
        if velvetg_conf['-long_mult_cutoff'] != None:
            command_line += '-long_mult_cutoff '+str(velvetg_conf['-long_mult_cutoff'])+' '
        if velvetg_conf['-alignments'] != None:
            command_line += '-alignments '+str(velvetg_conf['-alignments'])+' '
        if velvetg_conf['-exportFiltered'] != None:
            command_line += '-exportFiltered '+str(velvetg_conf['-exportFiltered'])+' '
        if velvetg_conf['-clean'] != None:
            command_line += '-clean '+str(velvetg_conf['-clean'])+' '
        if velvetg_conf['-very_clean'] != None:
            command_line += '-very_clean '+str(velvetg_conf['-very_clean'])+' '
        if velvetg_conf['-paired_exp_fraction'] != None:
            command_line += '-paired_exp_fraction '+str(velvetg_conf['-paired_exp_fraction'])+' '
        if velvetg_conf['-conserveLong'] != None:
            command_line += '-conserveLong '+str(velvetg_conf['-conserveLong'])
        subprocess.run(command_line, shell=True, check=True)
        print('end velvet_single_end')
    
    def velvet_paired(self):
        print('begin velvet_paired_end')
        velveth_conf = self.conf['velvet']['velveth']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velveth '+self.result_dir+'/velvet_output/ '
        if velveth_conf['hash_length'] != None:
            command_line += str(velveth_conf['hash_length'])+' -fastq '
        else:
            command_line += "31 -fastq "
        if velveth_conf['-short'] != None:
            command_line += "-short "
        elif velveth_conf['-short2'] != None:
            command_line += '-short2 '
        elif velveth_conf['-long'] != None:
            command_line += '-long'
        else:
            command_line += "-short "
        command_line += '-separate '
        command_line += self.input_file_1+' '+self.input_file_2
        subprocess.run(command_line, shell=True, check=True)
        
        velvetg_conf = self.conf['velvet']['velvetg']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velvetg '+self.result_dir+'/velvet_output/ '
        if velvetg_conf['-cov_cutoff'] != None:
            command_line += '-cov_cutoff '+str(velvetg_conf['-cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-read_trkg'] != None:
            command_line += '-read_trkg '+str(velvetg_conf['-read_trkg'])+' '
        if velvetg_conf['-min_contig_lgth'] != None:
            command_line += '-min_contig_lgth '+str(velvetg_conf['-min_contig_lgth'])+' '
        if velvetg_conf['-amos_file'] != None:
            command_line += '-amos_file '+str(velvetg_conf['-amos_file'])+' '
        if velvetg_conf['-exp_cov'] != None:
            command_line += '-exp_cov '+str(velvetg_conf['-exp_cov'])+' '
        if velvetg_conf['-long_cov_cutoff'] != None:
            command_line += '-long_cov_cutoff '+str(velvetg_conf['-long_cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-ins_length_long'] != None:
            command_line += '-ins_length_long '+str(velvetg_conf['-ins_length_long'])+' '
        if velvetg_conf['-ins_length*_sd'] != None:
            command_line += '-ins_length*_sd '+str(velvetg_conf['-ins_length*_sd'])+' '
        if velvetg_conf['-scaffolding'] != None:
            command_line += '-scaffolding '+str(velvetg_conf['-scaffolding'])+' '
        if velvetg_conf['-max_branch_length'] != None:
            command_line += '-max_branch_length '+str(velvetg_conf['-max_branch_length'])+' '
        if velvetg_conf['-max_divergence'] != None:
            command_line += '-max_divergence '+str(velvetg_conf['-max_divergence'])+' '
        if velvetg_conf['-max_gap_count'] != None:
            command_line += '-max_gap_count '+str(velvetg_conf['-max_gap_count'])+' '
        if velvetg_conf['-min_pair_count'] != None:
            command_line += '-min_pair_count '+str(velvetg_conf['-min_pair_count'])+' '
        if velvetg_conf['-max_coverage'] != None:
            command_line += '-max_coverage '+str(velvetg_conf['-max_coverage'])+' '
        if velvetg_conf['-coverage_mask'] != None:
            command_line += '-coverage_mask '+str(velvetg_conf['-coverage_mask'])+' '
        if velvetg_conf['-long_mult_cutoff'] != None:
            command_line += '-long_mult_cutoff '+str(velvetg_conf['-long_mult_cutoff'])+' '
        if velvetg_conf['-alignments'] != None:
            command_line += '-alignments '+str(velvetg_conf['-alignments'])+' '
        if velvetg_conf['-exportFiltered'] != None:
            command_line += '-exportFiltered '+str(velvetg_conf['-exportFiltered'])+' '
        if velvetg_conf['-clean'] != None:
            command_line += '-clean '+str(velvetg_conf['-clean'])+' '
        if velvetg_conf['-very_clean'] != None:
            command_line += '-very_clean '+str(velvetg_conf['-very_clean'])+' '
        if velvetg_conf['-paired_exp_fraction'] != None:
            command_line += '-paired_exp_fraction '+str(velvetg_conf['-paired_exp_fraction'])+' '
        if velvetg_conf['-conserveLong'] != None:
            command_line += '-conserveLong '+str(velvetg_conf['-conserveLong'])
        subprocess.run(command_line, shell=True, check=True)
        print('end velvet_paired_end')
    
    def velvet_interleaved(self):
        print('begin velvet_interleaved')
        velveth_conf = self.conf['velvet']['velveth']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velveth '+self.result_dir+'/velvet_output/ '
        if velveth_conf['hash_length'] != None:
            command_line += str(velveth_conf['hash_length'])+' -fastq '
        else:
            command_line += "31 -fastq "
        if velveth_conf['-short'] != None:
            command_line += "-short "
        elif velveth_conf['-short2'] != None:
            command_line += '-short2 '
        elif velveth_conf['-long'] != None:
            command_line += '-long'
        else:
            command_line += "-short "
        command_line += '-interleaved '
        command_line += self.input_file_12
        subprocess.run(command_line, shell=True, check=True)

        velvetg_conf = self.conf['velvet']['velvetg']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/velvetg '+self.result_dir+'/velvet_output/ '
        if velvetg_conf['-cov_cutoff'] != None:
            command_line += '-cov_cutoff '+str(velvetg_conf['-cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-read_trkg'] != None:
            command_line += '-read_trkg '+str(velvetg_conf['-read_trkg'])+' '
        if velvetg_conf['-min_contig_lgth'] != None:
            command_line += '-min_contig_lgth '+str(velvetg_conf['-min_contig_lgth'])+' '
        if velvetg_conf['-amos_file'] != None:
            command_line += '-amos_file '+str(velvetg_conf['-amos_file'])+' '
        if velvetg_conf['-exp_cov'] != None:
            command_line += '-exp_cov '+str(velvetg_conf['-exp_cov'])+' '
        if velvetg_conf['-long_cov_cutoff'] != None:
            command_line += '-long_cov_cutoff '+str(velvetg_conf['-long_cov_cutoff'])+' '
        if velvetg_conf['-ins_length'] != None:
            command_line += '-ins_length '+str(velvetg_conf['-ins_length'])+' '
        if velvetg_conf['-ins_length_long'] != None:
            command_line += '-ins_length_long '+str(velvetg_conf['-ins_length_long'])+' '
        if velvetg_conf['-ins_length*_sd'] != None:
            command_line += '-ins_length*_sd '+str(velvetg_conf['-ins_length*_sd'])+' '
        if velvetg_conf['-scaffolding'] != None:
            command_line += '-scaffolding '+str(velvetg_conf['-scaffolding'])+' '
        if velvetg_conf['-max_branch_length'] != None:
            command_line += '-max_branch_length '+str(velvetg_conf['-max_branch_length'])+' '
        if velvetg_conf['-max_divergence'] != None:
            command_line += '-max_divergence '+str(velvetg_conf['-max_divergence'])+' '
        if velvetg_conf['-max_gap_count'] != None:
            command_line += '-max_gap_count '+str(velvetg_conf['-max_gap_count'])+' '
        if velvetg_conf['-min_pair_count'] != None:
            command_line += '-min_pair_count '+str(velvetg_conf['-min_pair_count'])+' '
        if velvetg_conf['-max_coverage'] != None:
            command_line += '-max_coverage '+str(velvetg_conf['-max_coverage'])+' '
        if velvetg_conf['-coverage_mask'] != None:
            command_line += '-coverage_mask '+str(velvetg_conf['-coverage_mask'])+' '
        if velvetg_conf['-long_mult_cutoff'] != None:
            command_line += '-long_mult_cutoff '+str(velvetg_conf['-long_mult_cutoff'])+' '
        if velvetg_conf['-alignments'] != None:
            command_line += '-alignments '+str(velvetg_conf['-alignments'])+' '
        if velvetg_conf['-exportFiltered'] != None:
            command_line += '-exportFiltered '+str(velvetg_conf['-exportFiltered'])+' '
        if velvetg_conf['-clean'] != None:
            command_line += '-clean '+str(velvetg_conf['-clean'])+' '
        if velvetg_conf['-very_clean'] != None:
            command_line += '-very_clean '+str(velvetg_conf['-very_clean'])+' '
        if velvetg_conf['-paired_exp_fraction'] != None:
            command_line += '-paired_exp_fraction '+str(velvetg_conf['-paired_exp_fraction'])+' '
        if velvetg_conf['-conserveLong'] != None:
            command_line += '-conserveLong '+str(velvetg_conf['-conserveLong'])
        subprocess.run(command_line, shell=True, check=True)
        print('end velvet_interleaved')
    
    def canu(self):
        print('begin canu')
        canu_conf = self.conf['canu']
        command_line = os.path.dirname(os.path.realpath(__file__))+'/external_tools/canu-2.0/bin/canu -p canu_assembly_result -d '+self.result_dir+'/canu_output/ '
        if canu_conf['genomeSize='] != None:
            command_line += 'genomeSize='+str(canu_conf['genomeSize='])+' '
        else:
            command_line += 'genomeSize=4.8m '
        if canu_conf['minReadLength='] != None:
            command_line += 'minReadLength='+str(int(canu_conf['minReadLength=']))+' '
        if canu_conf['minOverlapLength='] != None:
            command_line += 'minOverlapLength='+str(int(canu_conf['minOverlapLength=']))+' '
        if canu_conf['-pacbio-raw'] != None:
            command_line += '-pacbio-raw '
        elif canu_conf['-pacbio-corrected'] != None:
            command_line += '-pacbio-corrected '
        elif canu_conf['-nanopore-raw'] != None:
            command_line += '-nanopore-raw '
        elif canu_conf['-nanopore-corrected'] != None:
            command_line += '-nanopore-corrected '
        else:
            command_line += '-pacbio-raw '
        command_line += self.input_file
        subprocess.run(command_line, shell=True, check=True)
        print('end canu')
    
def assembly_single_end(input_file, result_dir):
    print("Begin assembly")
    print("input_file="+input_file)
    # result = subprocess.run('megahit -r '+input_file+' -o '+result_dir+'/assembly', shell=True, check=True)
    print("Begin megahit")
    subprocess.run('megahit -r '+input_file+' -o '+result_dir+'/assembly/megahit_out', shell=True, check=True)
    # print("result of megahit:")
    # print(result.stdout)
    print("End megahit")
    print("Begin QUAST")
    subprocess.run('quast.py '+result_dir+'/assembly/megahit_out/final.contigs.fa -o '+result_dir+'/assembly/quast_out', shell=True, check=True)
    print("End QUAST")
    print("End assembly")

def assembly_paired_end(input_file_1, input_file_2, result_dir):
    print("Begin assembly")
    print("input_file="+input_file_1+input_file_2)
    # result = subprocess.run('megahit -r '+input_file+' -o '+result_dir+'/assembly', shell=True, check=True)
    print("Begin megahit")
    subprocess.run('megahit -1 '+input_file_1+' -2 '+input_file_2+' -o '+result_dir+'/assembly/megahit_out', shell=True, check=True)
    # print("result of megahit:")
    # print(result.stdout)
    print("End megahit")
    print("Begin QUAST")
    subprocess.run('quast.py '+result_dir+'/assembly/megahit_out/final.contigs.fa -o '+result_dir+'/assembly/quast_out', shell=True, check=True)
    print("End QUAST")
    print("End assembly")
