import preprocessing
import annotation
# import denovo
import os

class ThirdGenerationSequencing:

    input_file = None
    result_dir = None
    conf = None

    def __init__(self, result_dir, conf, input_file):
        self.result_dir = result_dir
        self.conf = conf
        self.input_file = input_file

    def run(self):
        if  self.conf['preprocessing']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'preprocessing')
            preprocessing_obj = preprocessing.Preprocessing(self.result_dir, self.conf, input_file=self.input_file)
            if self.conf['preprocessing']['fastqc']['enable'] != False:
                preprocessing_obj.fastqc_single_end('.')
                temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
                temp_file.write('<ul>\n')
                temp_file.write('<li>preprocessing result is in %s</li>\n' % './preprocessing')
                temp_file.write('<li><a href="%s">click to report</a></li>\n' % ('./preprocessing/'))
                temp_file.write('</ul>\n')
                temp_file.close()

        if  self.conf['identification']['enable'] != False:
            os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'identification')
            resequencing_obj = annotation.Resequencing(self.result_dir, self.conf, self.input_file)
            resequencing_obj.run_3gs()
        # if  self.conf['denovo']['enable'] != None:
        #     os.mkdir(os.path.abspath('.') + '/' + self.result_dir + '/' + 'denovo')
        #     denovo_obj = denovo.Denovo(self.result_dir, self.conf, input_file=self.input_file)
        #     denovo_obj.run_3gs()

