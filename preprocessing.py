import subprocess
import os

class Preprocessing:

    result_dir = None
    conf = None
    input_file = None
    input_file_1 = None
    input_file_2 = None

    def __init__(self, result_dir, conf, input_file=None, input_file_1=None, input_file_2=None):
        self.result_dir = result_dir
        self.conf = conf
        self.input_file = input_file
        self.input_file_1 = input_file_1
        self.input_file_2 = input_file_2

    def fastqc_single_end(self, folder_name):
        print("begin fastqc single end")
        fastqc_conf = self.conf['preprocessing']['fastqc']
        com = 'fastqc -o '+self.result_dir+'/preprocessing/'+folder_name+' '
        if fastqc_conf['--casava'] != None:
            com += "--casava "
        if fastqc_conf['--nofilter'] != None:
            com += "--nofilter "
        if fastqc_conf['--nogroup'] != None:
            com += "--nogroup "
        if fastqc_conf['-t'] != None:
            com += "-t %s " % int(fastqc_conf['-t'])
        if fastqc_conf['-c'] != None:
            com += "-c "+str(fastqc_conf['-c'])+' '
        if fastqc_conf['-a'] != None:
            com += "-a "+str(fastqc_conf['-a'])+' '
        if fastqc_conf['-l'] != None:
            com += "-l "+str(fastqc_conf['-l'])+' '
        if fastqc_conf['-k'] != None:
            com += "-k %s " % int(fastqc_conf['-k'])
        com += self.input_file
        try:
            completed_process = subprocess.run(com, shell=True)
            if completed_process.returncode == 0:
                print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
            else:
                print('An error occurred in Assembly. Please install fastqc.')
                print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
                completed_process = subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/FastQC/'+com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('An error occurred in Assembly. Please install fastqc.')
            exit()
        print("end fastqc single end")
    
    def fastqc_paired_end(self, folder_name):
        print("begin fastqc paired end")
        fastqc_conf = self.conf['preprocessing']['fastqc']
        com = 'fastqc -o '+self.result_dir+'/preprocessing/'+folder_name+' '
        if fastqc_conf['--casava'] != None:
            com += "--casava "
        if fastqc_conf['--nofilter'] != None:
            com += "--nofilter "
        if fastqc_conf['--nogroup'] != None:
            com += "--nogroup "
        if fastqc_conf['-t'] != None:
            com += "-t %s " % int(fastqc_conf['-t'])
        if fastqc_conf['-c'] != None:
            com += "-c "+str(fastqc_conf['-c'])+' '
        if fastqc_conf['-a'] != None:
            com += "-a "+str(fastqc_conf['-a'])+' '
        if fastqc_conf['-l'] != None:
            com += "-l "+str(fastqc_conf['-l'])+' '
        if fastqc_conf['-k'] != None:
            com += "-k %s " % int(fastqc_conf['-k'])
        com += self.input_file_1+" "+self.input_file_2
        try:
            completed_process = subprocess.run(com, shell=True)
            if completed_process.returncode == 0:
                print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
            else:
                print('An error occurred in Assembly. Please install fastqc.')
                print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
                completed_process = subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/FastQC/'+com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('An error occurred in Assembly. Please install fastqc.')
            exit()
        print("end fastqc paired end")
    
    def fastp_single_end(self):
        print("begin fastp_single_end")
        fastp_conf = self.conf['preprocessing']['fastp']
        com = 'fastp -i '+self.input_file+' -o '+self.result_dir+'/preprocessing/fastp_output.fastq -j '+self.result_dir+'/preprocessing/fastp.json -h '+self.result_dir+'/preprocessing/fastp.html '
        if fastp_conf['--phred64'] != None:
            com += '--phred64 '
        if fastp_conf['-V'] != None:
            com += '-V '
        if fastp_conf['-A'] != None:
            com += '-A '
        if fastp_conf['--adapter_sequence'] != None:
            com += '--adapter_sequence '+fastp_conf['--adapter_sequence']+' '
        # if fastp_conf['--adapter_sequence_r2'] != None:
        #     com += '--adapter_sequence_r2 '+fastp_conf['--adapter_sequence_r2']+' '
        if fastp_conf['--adapter_fasta'] != None:
            com += '--adapter_fasta '+fastp_conf['--adapter_fasta']+' '
        # if fastp_conf['--detect_adapter_for_pe'] != None:
        #     com += '--detect_adapter_for_pe '
        if fastp_conf['-f'] != None:
            com += '-f %s ' % int(fastp_conf['-f'])
        if fastp_conf['-t'] != None:
            com += '-t %s ' % int(fastp_conf['-t'])
        if fastp_conf['-b'] != None:
            com += '-b %s ' % int(fastp_conf['-b'])
        # if fastp_conf['-F'] != None:
        #     com += '-F '+str(fastp_conf['-F'])+' '
        # if fastp_conf['-T'] != None:
        #     com += '-T '+str(fastp_conf['-T'])+' '
        # if fastp_conf['-B'] != None:
        #     com += '-B '+str(fastp_conf['-B'])+' '
        if fastp_conf['--trim_poly_g'] != None:
            com += '--trim_poly_g '
        if fastp_conf['--poly_g_min_len'] != None:
            com += '--poly_g_min_len %s ' % int(fastp_conf['--poly_g_min_len'])
        if fastp_conf['-G'] != None:
            com += '-G '
        if fastp_conf['--trim_poly_x'] != None:
            com += '--trim_poly_x '
        if fastp_conf['--poly_x_min_len'] != None:
            com += '--poly_x_min_len %s ' % int(fastp_conf['--poly_x_min_len'])
        if fastp_conf['--cut_front'] != None:
            com += '--cut_front '
        if fastp_conf['--cut_tail'] != None:
            com += '--cut_tail '
        if fastp_conf['-r'] != None:
            com += '-r '
        if fastp_conf['-W'] != None:
            com += "-W %s " % int(fastp_conf['-W'])
        if fastp_conf['--cut_mean_quality'] != None:
            com += "--cut_mean_quality %s " % int(fastp_conf['--cut_mean_quality'])
        if fastp_conf['--cut_front_window_size'] != None:
            com += "--cut_front_window_size %s " % int(fastp_conf['--cut_front_window_size'])
        if fastp_conf['--cut_front_mean_quality'] != None:
            com += "--cut_front_mean_quality %s " % int(fastp_conf['--cut_front_mean_quality'])
        if fastp_conf['--cut_tail_window_size'] != None:
            com += "--cut_tail_window_size %s " % int(fastp_conf['--cut_tail_window_size'])
        if fastp_conf['--cut_tail_mean_quality'] != None:
            com += "--cut_tail_mean_quality %s " % int(fastp_conf['--cut_tail_mean_quality'])
        if fastp_conf['--cut_right_window_size'] != None:
            com += "--cut_right_window_size %s " % int(fastp_conf['--cut_right_window_size'])
        if fastp_conf['--cut_right_mean_quality'] != None:
            com += "--cut_right_mean_quality %s " % int(fastp_conf['--cut_right_mean_quality'])
        if fastp_conf['-Q'] != None:
            com += '-Q '
        if fastp_conf['-q'] != None:
            com += "-q %s " % int(fastp_conf['-q'])
        if fastp_conf['-u'] != None:
            com += "-u %s " % int(fastp_conf['-u'])
        if fastp_conf['-n'] != None:
            com += "-n %s " % int(fastp_conf['-n'])
        if fastp_conf['-e'] != None:
            com += "-e %s " % int(fastp_conf['-e'])
        if fastp_conf['-L'] != None:
            com += "-L "
        if fastp_conf['--length_required'] != None:
            com += "--length_required %s " % int(fastp_conf['--length_required'])
        if fastp_conf['--length_limit'] != None:
            com += "--length_limit %s " % int(fastp_conf['--length_limit'])
        if fastp_conf['--low_complexity_filter'] != None:
            com += "--low_complexity_filter "
        if fastp_conf['--complexity_threshold'] != None:
            com += "--complexity_threshold %s " % int(fastp_conf['--complexity_threshold'])
        if fastp_conf['--filter_by_index1'] != None:
            com += "--filter_by_index1 "+str(fastp_conf['--filter_by_index1'])+' '
        if fastp_conf['--filter_by_index2'] != None:
            com += "--filter_by_index2 "+str(fastp_conf['--filter_by_index2'])+' '
        if fastp_conf['--filter_by_index_threshold'] != None:
            com += "--filter_by_index_threshold %s " % int(fastp_conf['--filter_by_index_threshold'])
        # if fastp_conf['--correction'] != None:
        #     com += "--correction "
        # if fastp_conf['--overlap_len_require'] != None:
        #     com += "--overlap_len_require "+str(fastp_conf['--overlap_len_require'])+' '
        # if fastp_conf['--overlap_diff_limit'] != None:
        #     com += "--overlap_diff_limit "+str(fastp_conf['--overlap_diff_limit'])+' '
        # if fastp_conf['--overlap_diff_percent_limit'] != None:
        #     com += "--overlap_diff_percent_limit "+str(fastp_conf['--overlap_diff_percent_limit'])+' '
        if fastp_conf['--umi'] != None:
            com += '--umi '
        if fastp_conf['--umi_loc'] != None:
            com += '--umi_loc '+fastp_conf['--umi_loc']+' '
        if fastp_conf['--umi_len'] != None:
            com += '--umi_len %s ' % int(fastp_conf['--umi_len'])
        if fastp_conf['--umi_prefix'] != None:
            com += '--umi_prefix '+fastp_conf['--umi_prefix']+' '
        if fastp_conf['--umi_skip'] != None:
            com += '--umi_skip %s ' % int(fastp_conf['--umi_skip'])
        if fastp_conf['-p'] != None:
            com += '-p '
        if fastp_conf['-P'] != None:
            com += '-P %s ' % int(fastp_conf['-P'])
        if fastp_conf['-w'] != None:
            com += '-w %s' % int(fastp_conf['-w'])

        completed_process = subprocess.run(com, shell=True)
        if completed_process.returncode == 0:
            print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
        else:
            print('An error occurred in Assembly. Please install fastp.')
            print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
            try:
                completed_process = subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/'+com, shell=True, check=True)
            except Exception as e:
                print(e)
                print('An error occurred in Assembly. Please install fastp.')
                exit()
        print("end fastp_single_end")
    
    def fastp_paired_end(self):
        print("begin fastp_paired_end")
        fastp_conf = self.conf['preprocessing']['fastp']
        com = 'fastp --in1 '+self.input_file_1+" --in2 "+self.input_file_2+' --out1 '+self.result_dir+'/preprocessing/fastp_output_1.fastq --out2 '+self.result_dir+'/preprocessing/fastp_output_2.fastq -j '+self.result_dir+'/preprocessing/fastp.json -h '+self.result_dir+'/preprocessing/fastp.html '
        if fastp_conf['--phred64'] != None:
            com += '--phred64 '
        if fastp_conf['-V'] != None:
            com += '-V '
        if fastp_conf['-A'] != None:
            com += '-A '
        if fastp_conf['--adapter_sequence'] != None:
            com += '--adapter_sequence '+fastp_conf['--adapter_sequence']+' '
        if fastp_conf['--adapter_sequence_r2'] != None:
            com += '--adapter_sequence_r2 '+fastp_conf['--adapter_sequence_r2']+' '
        if fastp_conf['--adapter_fasta'] != None:
            com += '--adapter_fasta '+fastp_conf['--adapter_fasta']+' '
        if fastp_conf['--detect_adapter_for_pe'] != None:
            com += '--detect_adapter_for_pe '
        if fastp_conf['-f'] != None:
            com += '-f %s ' % int(fastp_conf['-f'])
        if fastp_conf['-t'] != None:
            com += '-t %s ' % int(fastp_conf['-t'])
        if fastp_conf['-b'] != None:
            com += '-b %s ' % int(fastp_conf['-b'])
        if fastp_conf['-F'] != None:
            com += '-F %s ' % int(fastp_conf['-F'])
        if fastp_conf['-T'] != None:
            com += '-T %s ' % int(fastp_conf['-T'])
        if fastp_conf['-B'] != None:
            com += '-B %s ' % int(fastp_conf['-B'])
        if fastp_conf['--trim_poly_g'] != None:
            com += '--trim_poly_g '
        if fastp_conf['--poly_g_min_len'] != None:
            com += '--poly_g_min_len %s ' % int(fastp_conf['--poly_g_min_len'])
        if fastp_conf['-G'] != None:
            com += '-G '
        if fastp_conf['--trim_poly_x'] != None:
            com += '--trim_poly_x '
        if fastp_conf['--poly_x_min_len'] != None:
            com += '--poly_x_min_len %s ' % int(fastp_conf['--poly_x_min_len'])
        if fastp_conf['--cut_front'] != None:
            com += '--cut_front '
        if fastp_conf['--cut_tail'] != None:
            com += '--cut_tail '
        if fastp_conf['-r'] != None:
            com += '-r '
        if fastp_conf['-W'] != None:
            com += "-W %s " % int(fastp_conf['-W'])
        if fastp_conf['--cut_mean_quality'] != None:
            com += "--cut_mean_quality %s " % int(fastp_conf['--cut_mean_quality'])
        if fastp_conf['--cut_front_window_size'] != None:
            com += "--cut_front_window_size %s " % int(fastp_conf['--cut_front_window_size'])
        if fastp_conf['--cut_front_mean_quality'] != None:
            com += "--cut_front_mean_quality %s " % int(fastp_conf['--cut_front_mean_quality'])
        if fastp_conf['--cut_tail_window_size'] != None:
            com += "--cut_tail_window_size %s " % int(fastp_conf['--cut_tail_window_size'])
        if fastp_conf['--cut_tail_mean_quality'] != None:
            com += "--cut_tail_mean_quality %s " % int(fastp_conf['--cut_tail_mean_quality'])
        if fastp_conf['--cut_right_window_size'] != None:
            com += "--cut_right_window_size %s " % int(fastp_conf['--cut_right_window_size'])
        if fastp_conf['--cut_right_mean_quality'] != None:
            com += "--cut_right_mean_quality %s " % int(fastp_conf['--cut_right_mean_quality'])
        if fastp_conf['-Q'] != None:
            com += '-Q '
        if fastp_conf['-q'] != None:
            com += "-q %s " % int(fastp_conf['-q'])
        if fastp_conf['-u'] != None:
            com += "-u %s " % int(fastp_conf['-u'])
        if fastp_conf['-n'] != None:
            com += "-n %s " % int(fastp_conf['-n'])
        if fastp_conf['-e'] != None:
            com += "-e %s " % int(fastp_conf['-e'])
        if fastp_conf['-L'] != None:
            com += "-L "
        if fastp_conf['--length_required'] != None:
            com += "--length_required %s " % int(fastp_conf['--length_required'])
        if fastp_conf['--length_limit'] != None:
            com += "--length_limit %s " % int(fastp_conf['--length_limit'])
        if fastp_conf['--low_complexity_filter'] != None:
            com += "--low_complexity_filter "
        if fastp_conf['--complexity_threshold'] != None:
            com += "--complexity_threshold %s " % int(fastp_conf['--complexity_threshold'])
        if fastp_conf['--filter_by_index1'] != None:
            com += "--filter_by_index1 "+str(fastp_conf['--filter_by_index1'])+' '
        if fastp_conf['--filter_by_index2'] != None:
            com += "--filter_by_index2 "+str(fastp_conf['--filter_by_index2'])+' '
        if fastp_conf['--filter_by_index_threshold'] != None:
            com += "--filter_by_index_threshold %s " % int(fastp_conf['--filter_by_index_threshold'])
        if fastp_conf['--correction'] != None:
            com += "--correction "
        if fastp_conf['--overlap_len_require'] != None:
            com += "--overlap_len_require %s " % int(fastp_conf['--overlap_len_require'])
        if fastp_conf['--overlap_diff_limit'] != None:
            com += "--overlap_diff_limit %s " % int(fastp_conf['--overlap_diff_limit'])
        if fastp_conf['--overlap_diff_percent_limit'] != None:
            com += "--overlap_diff_percent_limit %s " % int(fastp_conf['--overlap_diff_percent_limit'])
        if fastp_conf['--umi'] != None:
            com += '--umi '
        if fastp_conf['--umi_loc'] != None:
            com += '--umi_loc '+fastp_conf['--umi_loc']+' '
        if fastp_conf['--umi_len'] != None:
            com += '--umi_len %s ' % int(fastp_conf['--umi_len'])
        if fastp_conf['--umi_prefix'] != None:
            com += '--umi_prefix '+fastp_conf['--umi_prefix']+' '
        if fastp_conf['--umi_skip'] != None:
            com += '--umi_skip %s ' % int(fastp_conf['--umi_skip'])
        if fastp_conf['-p'] != None:
            com += '-p '
        if fastp_conf['-P'] != None:
            com += '-P %s ' % int(fastp_conf['-P'])
        if fastp_conf['-w'] != None:
            com += '-w %s' % int(fastp_conf['-w'])
        completed_process = subprocess.run(com, shell=True)
        if completed_process.returncode == 0:
            print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
        else:
            print('An error occurred in Assembly. Please install fastp.')
            print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
            try:
                completed_process = subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/'+com, shell=True, check=True)
            except Exception as e:
                print(e)
                print('An error occurred in Assembly. Please install fastp.')
                exit()
        print("end fastp_paired_end")
    
    def trimmomatic_single_end(self):
        print("begin trimmomatic_single_end")
        trimmomatic_conf = self.conf['preprocessing']['trimmomatic']
        com = ''
        if trimmomatic_conf['-threads'] != None:
            com += "-threads %s " % int(trimmomatic_conf['-threads'])
        if trimmomatic_conf['-phred33'] != None:
            com += "-phred33 "
        elif trimmomatic_conf['-phred64'] != None:
            com += "-phred64 "
        if trimmomatic_conf['-validatePairs'] != None:
            com += "-validatePairs "
        com += self.input_file+" "+self.result_dir+'/preprocessing/trimmomatic_output.fastq '
        if trimmomatic_conf['ILLUMINACLIP'] != None:
            com += "ILLUMINACLIP:%s " % int(trimmomatic_conf['ILLUMINACLIP'])
        if trimmomatic_conf['LEADING'] != None:
            com += "LEADING:%s " % int(trimmomatic_conf['LEADING'])
        else:
            com += "LEADING:3 "
        if trimmomatic_conf['TRAILING'] != None:
            com += "TRAILING:%s " % int(trimmomatic_conf['TRAILING'])
        else:
            com += "TRAILING:3 "
        if trimmomatic_conf['SLIDINGWINDOW'] != None:
            com += "SLIDINGWINDOW:"+str(trimmomatic_conf['SLIDINGWINDOW'])+' '
        else:
            com += "SLIDINGWINDOW:4:15 "
        if trimmomatic_conf['MINLEN'] != None:
            com += "MINLEN:%s" % int(trimmomatic_conf['MINLEN'])
        else:
            com += "MINLEN:36"

        completed_process = subprocess.run('trimmomatic SE '+com, shell=True)
        if completed_process.returncode == 0:
            print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
        else:
            print('An error occurred in Assembly. Please install trimmomatic.')
            print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
            try:
                completed_process = subprocess.run('java -jar %s/external_tools/trimmomatic-0.39.jar SE ' % os.path.dirname(os.path.realpath(__file__))+com, shell=True, check=True)
            except Exception as e:
                print(e)
                print('An error occurred in Assembly. Please install trimmomatic.')
                exit()
        print("end trimmomatic_single_end")
        
    def trimmomatic_paired_end(self):
        print("begin trimmomatic_paired_end")
        trimmomatic_conf = self.conf['preprocessing']['trimmomatic']
        com = ''
        if trimmomatic_conf['-threads'] != None:
            com += "-threads %s " % int(trimmomatic_conf['-threads'])
        if trimmomatic_conf['-phred33'] != None:
            com += "-phred33 "
        elif trimmomatic_conf['-phred64'] != None:
            com += "-phred64 "
        if trimmomatic_conf['-validatePairs'] != None:
            com += "-validatePairs "
        com += self.input_file_1+" "+self.input_file_2+" "+self.result_dir+'/preprocessing/paired_output_1.fastq '+self.result_dir+'/preprocessing/unpaired_output_1.fastq '+self.result_dir+'/preprocessing/paired_output_2.fastq '+self.result_dir+'/preprocessing/unpaired_output_2.fastq '
        if trimmomatic_conf['ILLUMINACLIP'] != None:
            com += "ILLUMINACLIP:%s " % int(trimmomatic_conf['ILLUMINACLIP'])
        if trimmomatic_conf['LEADING'] != None:
            com += "LEADING:%s " % int(trimmomatic_conf['LEADING'])
        else:
            com += "LEADING:3 "
        if trimmomatic_conf['TRAILING'] != None:
            com += "TRAILING:%s " % int(trimmomatic_conf['TRAILING'])
        else:
            com += "TRAILING:3 "
        if trimmomatic_conf['SLIDINGWINDOW'] != None:
            com += "SLIDINGWINDOW:"+str(trimmomatic_conf['SLIDINGWINDOW'])+' '
        else:
            com += "SLIDINGWINDOW:4:15 "
        if trimmomatic_conf['MINLEN'] != None:
            com += "MINLEN:%s" % int(trimmomatic_conf['MINLEN'])
        else:
            com += "MINLEN:36"
        
        completed_process = subprocess.run('trimmomatic PE '+com, shell=True)
        if completed_process.returncode == 0:
            print('Preprocessing runs successfully! CompleteProcess.returncode = %s.' % completed_process.returncode)
        else:
            print('An error occurred in Assembly. Please install trimmomatic.')
            print('stdout = %s, stderr = %s.' % (completed_process.stdout, completed_process.stderr))
            try:
                completed_process = subprocess.run('java -jar %s/external_tools/trimmomatic-0.39.jar PE ' % os.path.dirname(os.path.realpath(__file__))+com, shell=True, check=True)
            except Exception as e:
                print(e)
                print('An error occurred in Assembly. Please install trimmomatic.')
                exit()
        print("end trimmomatic_paired_end")

    def cutadapt_single_end(self):
        print("begin cutadapt_single_end")
        cutadapt_conf = self.conf['preprocessing']['cutadapt']
        com = 'cutadapt '
        if cutadapt_conf['-a'] != None:
            com += "-a "+cutadapt_conf['-a']+' '
        if cutadapt_conf['-g'] != None:
            com += "-g "+cutadapt_conf['-g']+' '
        if cutadapt_conf['-b'] != None:
            com += "-b "+cutadapt_conf['-b']+' '
        if cutadapt_conf['-e'] != None:
            com += "-e %s " % int(cutadapt_conf['-e'])
        if cutadapt_conf['--no-indels'] != None:
            com += "--no-indels "
        if cutadapt_conf['-n'] != None:
            com += "-n %s " % int(cutadapt_conf['-n'])
        if cutadapt_conf['-O'] != None:
            com += "-O %s " % int(cutadapt_conf['-O'])
        if cutadapt_conf['--match-read-wildcards'] != None:
            com += "--match-read-wildcards "
        if cutadapt_conf['-N'] != None:
            com += "-N "
        if cutadapt_conf['-u'] != None:
            com += "-u "+str(cutadapt_conf['-u'])+' '
        if cutadapt_conf['--nextseq-trim'] != None:
            com += "--nextseq-trim "+str(cutadapt_conf['--nextseq-trim'])+' '
        if cutadapt_conf['-q'] != None:
            com += "-q "+str(cutadapt_conf['-q'])+' '
        if cutadapt_conf['--quality-base'] != None:
            com += "--quality-base %s " % int(cutadapt_conf['--quality-base'])
        if cutadapt_conf['--length'] != None:
            com += "--length "+str(cutadapt_conf['--length'])+' '
        if cutadapt_conf['--trim-n'] != None:
            com += "--trim-n "
        if cutadapt_conf['--length-tag'] != None:
            com += "--length-tag "+cutadapt_conf['--length-tag']+' '
        if cutadapt_conf['--strip-suffix'] != None:
            com += "--strip-suffix "+cutadapt_conf['--strip-suffix']+' '
        if cutadapt_conf['-x'] != None:
            com += "-x "+cutadapt_conf['-x']+' '
        if cutadapt_conf['-y'] != None:
            com += "-y "+cutadapt_conf['-y']+' '
        if cutadapt_conf['--zero-cap'] != None:
            com += "--zero-cap "+cutadapt_conf['--zero-cap']+' '
        if cutadapt_conf['-m'] != None:
            com += "-m %s " % int(cutadapt_conf['-m'])
        if cutadapt_conf['-M'] != None:
            com += "-M "+str(cutadapt_conf['-M'])+' '
        if cutadapt_conf['--max-n'] != None:
            com += "--max-n "+str(cutadapt_conf['--max-n'])+' '
        if cutadapt_conf['--discard-trimmed'] != None:
            com += "--discard-trimmed "
        if cutadapt_conf['--discard-untrimmed'] != None:
            com += "--discard-untrimmed "
        if cutadapt_conf['--discard-casava'] != None:
            com += "--discard-casava "
        com += '-o '+self.result_dir+'/preprocessing/cutadapt_output.fastq '+self.input_file
        try:
            subprocess.run(com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('Please install cutadapt.')
            exit()
        print("end cutadapt_single_end")

    def cutadapt_paired_end(self):
        print("begin cutadapt_paired_end")
        cutadapt_conf = self.conf['preprocessing']['cutadapt']
        com = 'cutadapt '
        if cutadapt_conf['-A'] != None:
            com += "-A "+cutadapt_conf['-A']+' '
        if cutadapt_conf['-G'] != None:
            com += "-G "+cutadapt_conf['-G']+' '
        if cutadapt_conf['-B'] != None:
            com += "-B "+cutadapt_conf['-B']+' '
        if cutadapt_conf['-U'] != None:
            com += "-U "+str(cutadapt_conf['-U'])+' '
        if cutadapt_conf['-e'] != None:
            com += "-e %s " % int(cutadapt_conf['-e'])
        if cutadapt_conf['--no-indels'] != None:
            com += "--no-indels "
        if cutadapt_conf['-n'] != None:
            com += "-n %s " % int(cutadapt_conf['-n'])
        if cutadapt_conf['-O'] != None:
            com += "-O %s " % int(cutadapt_conf['-O'])
        if cutadapt_conf['--match-read-wildcards'] != None:
            com += "--match-read-wildcards "
        if cutadapt_conf['-N'] != None:
            com += "-N "
        if cutadapt_conf['-u'] != None:
            com += "-u "+str(cutadapt_conf['-u'])+' '
        if cutadapt_conf['--nextseq-trim'] != None:
            com += "--nextseq-trim "+str(cutadapt_conf['--nextseq-trim'])+' '
        if cutadapt_conf['-q'] != None:
            com += "-q "+str(cutadapt_conf['-q'])+' '
        if cutadapt_conf['--quality-base'] != None:
            com += "--quality-base %s " % int(cutadapt_conf['--quality-base'])
        if cutadapt_conf['--length'] != None:
            com += "--length "+str(cutadapt_conf['--length'])+' '
        if cutadapt_conf['--trim-n'] != None:
            com += "--trim-n "
        if cutadapt_conf['--length-tag'] != None:
            com += "--length-tag "+cutadapt_conf['--length-tag']+' '
        if cutadapt_conf['--strip-suffix'] != None:
            com += "--strip-suffix "+cutadapt_conf['--strip-suffix']+' '
        if cutadapt_conf['-x'] != None:
            com += "-x "+cutadapt_conf['-x']+' '
        if cutadapt_conf['-y'] != None:
            com += "-y "+cutadapt_conf['-y']+' '
        if cutadapt_conf['--zero-cap'] != None:
            com += "--zero-cap "+cutadapt_conf['--zero-cap']+' '
        if cutadapt_conf['-m'] != None:
            com += "-m %s " % int(cutadapt_conf['-m'])
        if cutadapt_conf['-M'] != None:
            com += "-M "+str(cutadapt_conf['-M'])+' '
        if cutadapt_conf['--max-n'] != None:
            com += "--max-n "+str(cutadapt_conf['--max-n'])+' '
        if cutadapt_conf['--discard-trimmed'] != None:
            com += "--discard-trimmed "
        if cutadapt_conf['--discard-untrimmed'] != None:
            com += "--discard-untrimmed "
        if cutadapt_conf['--discard-casava'] != None:
            com += "--discard-casava "
        if cutadapt_conf['--pair-adapters'] != None:
            com += "--pair-adapters "
        if cutadapt_conf['--pair-filter'] != None:
            com += "--pair-filter "+cutadapt_conf['--pair-filter']+' '
        com += '-o '+self.result_dir+'/preprocessing/cutadapt_output_1.fastq -p '+self.result_dir+'/preprocessing/cutadapt_output_2.fastq '+self.input_file_1+' '+self.input_file_2
        try:
            subprocess.run(com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('Please install cutadapt.')
            exit()
        print("end cutadapt_paired_end")


    def sickle_single_end(self):
        print("begin sickle single end")
        sickle_conf = self.conf['preprocessing']['sickle']
        com = 'sickle se -f ' + self.input_file + ' -o '+self.result_dir+'/preprocessing/sickle_output.fastq '
        if sickle_conf['-t'] != None:
            com += "-t %s " % sickle_conf['-t']
        else:
            com += "-t illumina "
        if sickle_conf['-q'] != None:
            com += "-q %s " % sickle_conf['-q']
        if sickle_conf['-l'] != None:
            com += "-l %s " % sickle_conf['-l']
        if sickle_conf['-x'] != None:
            com += "-x "
        if sickle_conf['-n'] != None:
            com += "-n "
        try:
            subprocess.run(com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('Please install sickle.')
            exit()
        print("end sickle single end")


    def sickle_paired_end(self):
        print("begin sickle paired end")
        sickle_conf = self.conf['preprocessing']['sickle']
        com = 'sickle pe -f ' + self.input_file_1 + ' -r ' + self.input_file_2 + ' -o '+self.result_dir+'/preprocessing/sickle_output_1.fastq -p '+self.result_dir+'/preprocessing/sickle_output_2.fastq -s '+self.result_dir+'/preprocessing/sickle_trimmed_singles_file.fastq '
        if sickle_conf['-t'] != None:
            com += "-t %s " % sickle_conf['-t']
        else:
            com += "-t illumina "
        if sickle_conf['-q'] != None:
            com += "-q %s " % sickle_conf['-q']
        if sickle_conf['-l'] != None:
            com += "-l %s " % sickle_conf['-l']
        if sickle_conf['-x'] != None:
            com += "-x "
        if sickle_conf['-n'] != None:
            com += "-n "
        try:
            subprocess.run(com, shell=True, check=True)
        except Exception as e:
            print(e)
            print('Please install sickle.')
            exit()
        print("end sickle paired end")

    def soapnuke_single_end(self):
        print("begin soapnuke single end")
        sickle_conf = self.conf['preprocessing']['sickle']
        com = 'SOAPnuke filter -1 ' + self.input_file + ' -C '+'SOAPnuke_output.fastq.gz -o ' + self.result_dir+'/preprocessing/'
        
        subprocess.run(com, shell=True, check=True)
        subprocess.run("gunzip "+self.result_dir+'/preprocessing/SOAPnuke_output.fastq.gz', shell=True, check=True)
        print("end soapnuke single end")


    def soapnuke_paired_end(self):
        print("begin soapnuke paired end")
        sickle_conf = self.conf['preprocessing']['sickle']
        com = 'SOAPnuke filter -1 ' + self.input_file_1 + ' -2 ' + self.input_file_2 + ' -C '+'SOAPnuke_output_1.fastq.gz -D '+'SOAPnuke_output_2.fastq.gz -o ' + self.result_dir+'/preprocessing/'
        
        subprocess.run(com, shell=True, check=True)
        subprocess.run("gunzip "+self.result_dir+'/preprocessing/SOAPnuke_output_1.fastq.gz', shell=True, check=True)
        subprocess.run("gunzip "+self.result_dir+'/preprocessing/SOAPnuke_output_2.fastq.gz', shell=True, check=True)
        print("end soapnuke paired end")


def preprocessing_single_end(input_file, result_dir):
    print("Begin preprocessing")
    print("input_file="+input_file)
    subprocess.run('fastqc -o '+result_dir+'/preprocessing/ '+input_file, shell=True, check=True)
    subprocess.run('java -jar trimmomatic-0.38.jar SE '+input_file+" "+result_dir+'/preprocessing/output.fq.gz ILLUMINACLIP:TruSeq3-SE.fa:2:30:10 LEADING:2 TRAILING:2 SLIDINGWINDOW:4:2 MINLEN:25', shell=True, check=True)
    print("End preprocessing")

def preprocessing_paired_end(input_file_1, input_file_2, result_dir):
    print("Begin preprocessing")
    print("input_file="+input_file_1+input_file_2)
    subprocess.run('fastqc -o '+result_dir+'/preprocessing/ '+input_file_1+" "+input_file_2, shell=True, check=True)
    subprocess.run('java -jar trimmomatic-0.38.jar PE '+input_file_1+" "+input_file_2+" "+result_dir+'/preprocessing/paired_output_1.fq.gz '+result_dir+'/preprocessing/unpaired_output_1.fq.gz '+result_dir+'/preprocessing/paired_output_2.fq.gz '+result_dir+'/preprocessing/unpaired_output_2.fq.gz '+' ILLUMINACLIP:TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36', shell=True, check=True)
    print("End preprocessing")
