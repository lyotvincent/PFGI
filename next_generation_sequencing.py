import preprocessing
import annotation
# import denovo
import os

class NextGenerationSequencing:

    input_file = None
    input_file_1 = None
    input_file_2 = None
    # input_file_12 = None
    result_dir = None
    conf = None

    preprocessing_output = None
    preprocessing_output_1 = None
    preprocessing_output_2 = None

    def __init__(self, result_dir, conf, input_file=None, input_file_1=None, input_file_2=None):
        self.result_dir = result_dir
        self.conf = conf
        self.input_file = input_file
        self.input_file_1 = input_file_1
        self.input_file_2 = input_file_2
        # self.input_file_12 = input_file_12

    def run_single(self):
        if self.conf['preprocessing']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing')
            preprocessing_obj = preprocessing.Preprocessing(self.result_dir, self.conf, input_file=self.input_file)
            
            if self.conf['preprocessing']['fastp']['enable'] != False:
                preprocessing_obj.fastp_single_end()
                self.preprocessing_output = self.result_dir+'/preprocessing/fastp_output.fastq'
            else:
                if self.conf['preprocessing']['fastqc']['enable'] != False:
                    os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_before_filtering')
                    preprocessing_obj.fastqc_single_end('fastqc_before_filtering')
                if self.conf['preprocessing']['trimmomatic']['enable'] != False:
                    preprocessing_obj.trimmomatic_single_end()
                    self.preprocessing_output = self.result_dir+'/preprocessing/trimmomatic_output.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file = self.preprocessing_output
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_single_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['cutadapt']['enable'] != False:
                    preprocessing_obj.cutadapt_single_end()
                    self.preprocessing_output = self.result_dir+'/preprocessing/cutadapt_output.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file = self.preprocessing_output
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_single_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['sickle']['enable'] != False:
                    preprocessing_obj.sickle_single_end()
                    self.preprocessing_output = self.result_dir+'/preprocessing/sickle_output.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file = self.preprocessing_output
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_single_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['SOAPnuke']['enable'] != False:
                    preprocessing_obj.soapnuke_single_end()
                    self.preprocessing_output = self.result_dir+'/preprocessing/SOAPnuke_output.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file = self.preprocessing_output
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_single_end('fastqc_after_filtering')
                else:
                    self.preprocessing_output = self.input_file
            temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
            temp_file.write('<ul>\n')
            temp_file.write('<li>preprocessing result is in %s</li>\n' % './preprocessing')
            temp_file.write('<li><a href="%s">click to report</a></li>\n' % ('./preprocessing/'))
            temp_file.write('</ul>\n')
            temp_file.close()
        else:
            self.preprocessing_output = self.input_file

        if self.conf['identification']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'identification')
            resequencing_obj = annotation.Resequencing(self.result_dir, self.conf, self.preprocessing_output)
            resequencing_obj.run()
        # if self.conf['denovo']['enable'] != False:
        #     os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'denovo')
        #     denovo_obj = denovo.Denovo(self.result_dir, self.conf, input_file=self.preprocessing_output)
        #     denovo_obj.run_single()

    def run_paired(self):
        if self.conf['preprocessing']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing')
            preprocessing_obj = preprocessing.Preprocessing(self.result_dir, self.conf, input_file_1=self.input_file_1, input_file_2=self.input_file_2)
            
            if self.conf['preprocessing']['fastp']['enable'] != False:
                preprocessing_obj.fastp_paired_end()
                self.preprocessing_output_1 = self.result_dir+'/preprocessing/fastp_output_1.fastq'
                self.preprocessing_output_2 = self.result_dir+'/preprocessing/fastp_output_2.fastq'
            else:
                if self.conf['preprocessing']['fastqc']['enable'] != False:
                    os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_before_filtering')
                    preprocessing_obj.fastqc_paired_end('fastqc_before_filtering')
                if self.conf['preprocessing']['trimmomatic']['enable'] != False:
                    preprocessing_obj.trimmomatic_paired_end()
                    self.preprocessing_output_1 = self.result_dir+'/preprocessing/paired_output_1.fastq'
                    self.preprocessing_output_2 = self.result_dir+'/preprocessing/paired_output_2.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file_1 = self.preprocessing_output_1
                        preprocessing_obj.input_file_2 = self.preprocessing_output_2
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_paired_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['cutadapt']['enable'] != False:
                    preprocessing_obj.cutadapt_paired_end()
                    self.preprocessing_output_1 = self.result_dir+'/preprocessing/cutadapt_output_1.fastq'
                    self.preprocessing_output_2 = self.result_dir+'/preprocessing/cutadapt_output_2.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file_1 = self.preprocessing_output_1
                        preprocessing_obj.input_file_2 = self.preprocessing_output_2
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_paired_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['sickle']['enable'] != False:
                    preprocessing_obj.sickle_paired_end()
                    self.preprocessing_output_1 = self.result_dir+'/preprocessing/sickle_output_1.fastq'
                    self.preprocessing_output_2 = self.result_dir+'/preprocessing/sickle_output_2.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file_1 = self.preprocessing_output_1
                        preprocessing_obj.input_file_2 = self.preprocessing_output_2
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_paired_end('fastqc_after_filtering')
                elif self.conf['preprocessing']['SOAPnuke']['enable'] != False:
                    preprocessing_obj.soapnuke_paired_end()
                    self.preprocessing_output_1 = self.result_dir+'/preprocessing/SOAPnuke_output_1.fastq'
                    self.preprocessing_output_2 = self.result_dir+'/preprocessing/SOAPnuke_output_2.fastq'
                    if self.conf['preprocessing']['fastqc']['enable'] != False:
                        preprocessing_obj.input_file_1 = self.preprocessing_output_1
                        preprocessing_obj.input_file_2 = self.preprocessing_output_2
                        os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing/fastqc_after_filtering')
                        preprocessing_obj.fastqc_paired_end('fastqc_after_filtering')
                else:
                    self.preprocessing_output_1 = self.input_file_1
                    self.preprocessing_output_2 = self.input_file_2
            temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
            temp_file.write('<ul>\n')
            temp_file.write('<li>preprocessing result is in %s</li>\n' % './preprocessing')
            temp_file.write('<li><a href="%s">click to report</a></li>\n' % ('./preprocessing/'))
            temp_file.write('</ul>\n')
            temp_file.close()
        else:
            self.preprocessing_output_1 = self.input_file_1
            self.preprocessing_output_2 = self.input_file_2
        
        print('preprocessing_output_1='+str(self.preprocessing_output_1))
        print('preprocessing_output_2='+str(self.preprocessing_output_2))

        if self.conf['identification']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'identification')
            resequencing_obj = annotation.Resequencing(self.result_dir, self.conf, self.preprocessing_output_1, self.preprocessing_output_2)
            resequencing_obj.run()
        # if self.conf['denovo']['enable'] != False:
        #     os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'denovo')
        #     denovo_obj = denovo.Denovo(self.result_dir, self.conf, input_file_1=self.preprocessing_output_1, input_file_2=self.preprocessing_output_2)
        #     denovo_obj.run_paired()

    # def run_interleaved(self):
    #     if self.conf['preprocessing']['enable'] != False:
    #         os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing')
    #         preprocessing_obj = preprocessing.Preprocessing(self.result_dir, self.conf, input_file=self.input_file_12)
    #         if self.conf['preprocessing']['fastqc']['enable'] != False:
    #             preprocessing_obj.fastqc_single_end()
    #             if self.conf['preprocessing']['trimmomatic']['enable'] != False:
    #                 preprocessing_obj.trimmomatic_single_end()
    #                 self.preprocessing_output = self.result_dir+'/preprocessing/trimmomatic_output.fastq'
    #             elif self.conf['preprocessing']['cutadapt']['enable'] != False:
    #                 preprocessing_obj.cutadapt_single_end()
    #                 self.preprocessing_output = self.result_dir+'/preprocessing/cutadapt_output.fastq'
    #             elif self.conf['preprocessing']['fastp']['enable'] != False:
    #                 preprocessing_obj.fastp_single_end()
    #                 self.preprocessing_output = self.result_dir+'/preprocessing/fastp_output.fastq'
    #             else:
    #                 self.preprocessing_output = self.input_file
    #         elif self.conf['preprocessing']['fastp']['enable'] != False:
    #             preprocessing_obj.fastp_single_end()
    #             self.preprocessing_output = self.result_dir+'/preprocessing/fastp_output.fastq'
    #         else:
    #             self.preprocessing_output = self.input_file_12
    #     else:
    #         self.preprocessing_output = self.input_file_12

    #     if self.conf['identification']['enable'] != False:
    #         os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'resequencing')
    #         resequencing_obj = resequencing.Resequencing(self.result_dir, self.conf, self.preprocessing_output)
    #         resequencing_obj.run()
    #     if self.conf['denovo']['enable'] != False:
    #         os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'denovo')
    #         denovo_obj = denovo.Denovo(self.result_dir, self.conf, input_file_12=self.preprocessing_output)
    #         denovo_obj.run_interleaved()