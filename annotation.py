from Bio.Blast.Applications import NcbiblastnCommandline
import subprocess
import os
import time

import assembly
import calculating_genome_similarity
import scripts.fasta2fastq
import scripts.fastq2fasta
import scripts.handle_blast_xml_result
import scripts.download_nucleotide
import scripts.download_gb
import scripts.identification
import scripts.genbank2gff3
import scripts.annotation_generator
import scripts.prokka_annotation

class Resequencing:

    result_dir = None
    conf = None
    input_file = None
    input_file_paired = None

    def __init__(self, result_dir, conf, input_file, input_file_paired=None):
        self.result_dir = result_dir
        self.conf = conf
        self.input_file = input_file
        self.input_file_paired = input_file_paired
    
    def run(self):

        print('Begin Resequencing')

        print('input_file='+str(self.input_file))
        
        assembly_conf = self.conf['identification']['assembly']
        if self.input_file_paired == None:
            print('begin assembly')
            os.mkdir(os.path.abspath('.')+'/'+self.result_dir+'/identification/assembly')
            assembly_obj = assembly.Assembly(self.result_dir+'/identification/assembly', assembly_conf, input_file=self.input_file)
            print(assembly_conf['megahit']['enable'], assembly_conf['spades']['enable'], assembly_conf['velvet']['enable'])
            if assembly_conf['megahit']['enable'] != False:
                assembly_obj.megahit_single()
                assembly_result = self.result_dir+'/identification/assembly/megahit_out/final.contigs.fa'
            elif assembly_conf['spades']['enable'] != False:
                assembly_obj.spades_single()
                assembly_result = self.result_dir+'/identification/assembly/spades_out/contigs.fasta'
            elif assembly_conf['velvet']['enable'] != False:
                assembly_obj.velvet_single()
                assembly_result = self.result_dir+'/identification/assembly/velvet_output/contigs.fa'
            # else:
            #     assembly_obj.megahit_single()
            #     assembly_result = self.result_dir+'/identification/assembly/megahit_out/final.contigs.fa'
            print('end assembly')
            print("Begin QUAST")
            subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/quast-5.0.2/quast.py '+assembly_result+' --min-contig 50 -o '+self.result_dir+'/identification/quast_out', shell=True, check=True)
            print("End QUAST")
        else:
            print('begin assembly')
            os.mkdir(os.path.abspath('.')+'/'+self.result_dir+'/identification/assembly')
            assembly_obj = assembly.Assembly(self.result_dir+'/identification/assembly', assembly_conf, input_file_1=self.input_file, input_file_2=self.input_file_paired)
            if assembly_conf['megahit']['enable'] != False:
                assembly_obj.megahit_paired()
                assembly_result = self.result_dir+'/identification/assembly/megahit_out/final.contigs.fa'
            elif assembly_conf['spades']['enable'] != False:
                assembly_obj.spades_paired()
                assembly_result = self.result_dir+'/identification/assembly/spades_out/contigs.fasta'
            elif assembly_conf['velvet']['enable'] != False:
                assembly_obj.velvet_paired()
                assembly_result = self.result_dir+'/identification/assembly/velvet_output/contigs.fa'
            # else:
            #     assembly_obj.megahit_paired()
            #     assembly_result = self.result_dir+'/identification/assembly/megahit_out/final.contigs.fa'
            print('end assembly')
            print("Begin QUAST")
            subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/quast-5.0.2/quast.py '+assembly_result+' --min-contig 50 -o '+self.result_dir+'/identification/quast_out', shell=True, check=True)
            print("End QUAST")
        
        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>assembly result is in %s</li>\n' % './identification/assembly')
        temp_file.write('<li><a href="%s">click to assembly result</a></li>\n' % ('./identification/assembly'))
        temp_file.write('<li>assembly qc result is in %s</li>\n' % './identification/quast_out')
        temp_file.write('<li><a href="%s">click to assembly qc result</a></li>\n' % ('./identification/quast_out/report.html'))
        temp_file.write('</ul>\n')
        temp_file.close()
        if assembly_conf['enable'] != False:
            blast_input = assembly_result
        else:
            scripts.fastq2fasta.fastq2fasta(self.input_file, self.result_dir+"/identification")
            blast_input = self.result_dir+"/identification/input.fasta"

        # time.sleep(1000)
        
        blastn_conf = self.conf['identification']['blastn']
        blastn_cline = NcbiblastnCommandline(cmd=os.path.dirname(os.path.realpath(__file__))+'/external_tools/blastn', query=blast_input, db=self.conf["identification"]['blastn']["blast_db_path"], outfmt=7, out=self.result_dir+"/identification/ncbi_fungi_blast_out.xml")
        blastn_cline.set_parameter('num_threads', int(blastn_conf['num_threads']))
        blastn_cline.set_parameter('num_alignments', int(blastn_conf['num_alignments']))
        blastn_cline.set_parameter('evalue', float(blastn_conf['evalue']))
        # if blastn_conf['task'] != None:
        #     blastn_cline.set_parameter('task', blastn_conf['task'])
        if blastn_conf['penalty'] != None:
            blastn_cline.set_parameter('penalty', int(blastn_conf['penalty']))
        if blastn_conf['reward'] != None:
            blastn_cline.set_parameter('reward', int(blastn_conf['reward']))
        # if blastn_conf['dust'] != None:
        #     blastn_cline.set_parameter('dust', blastn_conf['dust'])
        # if blastn_conf['filtering_db'] != None:
        #     blastn_cline.set_parameter('filtering_db', blastn_conf['filtering_db'])
        # if blastn_conf['window_masker_taxid'] != None:
        #     blastn_cline.set_parameter('window_masker_taxid', blastn_conf['window_masker_taxid'])
        # if blastn_conf['no_greedy'] != None:
        #     blastn_cline.set_parameter('no_greedy', blastn_conf['no_greedy'])
        # if blastn_conf['min_raw_gapped_score'] != None:
        #     blastn_cline.set_parameter('min_raw_gapped_score', blastn_conf['min_raw_gapped_score'])
        # if blastn_conf['ungapped'] != None:
        #     blastn_cline.set_parameter('ungapped', blastn_conf['ungapped'])
        # if blastn_conf['off_diagonal_range'] != None:
        #     blastn_cline.set_parameter('off_diagonal_range', blastn_conf['off_diagonal_range'])
        print(blastn_cline)
        stdout, stderr = blastn_cline()
        print(stdout)
        print(stderr)

        accession_version_list = scripts.handle_blast_xml_result.handle_blast_xml_result_outfmt7(self.result_dir+"/identification/ncbi_fungi_blast_out.xml")
        accession_version_list = [accession_version_list[i][0] for i in range(int(self.conf["identification"]['number_of_candidate_similar_genome']))]
        # print("accession_version_list="+str(accession_version_list))

        for accession_version in accession_version_list:
            scripts.download_nucleotide.download_by_accession_version(self.result_dir, accession_version)

        genome_similarity_calculator = calculating_genome_similarity.GenomeSimilarityCalculator(self.result_dir, assembly_result, accession_version_list)
        closest_accession_version, max_jaccard = genome_similarity_calculator.search_similar_genome_from_bacteria_dataset()
        print("closest_accession_version = %s, max_jaccard = %s" % (closest_accession_version, max_jaccard))

        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>closest accession version is %s in %s Jaccard similarity coefficient</li>\n' % (closest_accession_version, max_jaccard))
        temp_file.write('</ul>\n')
        temp_file.close()

        if self.conf['annotation']['cds_annotation']["enable"] != False:
            self.cds_annotation_ngs(closest_accession_version, assembly_result)

        if self.conf['annotation']['mlst'] != False:
            self.mlst(blast_input)

        if self.conf['annotation']['prokka']['enable'] != False:
            scripts.prokka_annotation.annotation(blast_input, self.result_dir, self.conf, closest_accession_version)


    def run_3gs(self):

        print('Begin Resequencing 3gs')

        assembly_conf = self.conf['identification']['assembly']
        os.mkdir(os.path.abspath('.')+'/'+self.result_dir+'/identification/assembly')
        assembly_obj = assembly.Assembly(self.result_dir+'/identification/assembly', assembly_conf, input_file=self.input_file)
        if assembly_conf['canu']['enable'] != False:
            assembly_obj.canu()
            assembly_result = self.result_dir+'/identification/assembly/canu_output/canu_assembly_result.contigs.fasta'
            print("Begin QUAST")
            subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/quast-5.0.2/quast.py '+assembly_result+' --min-contig 50 -o '+self.result_dir+'/identification/quast_out', shell=True, check=True)
            print("End QUAST")
        elif assembly_conf['spades']['enable'] != False:
            assembly_obj.spades_3gs()
            assembly_result = self.result_dir+'/identification/assembly/spades_out/contigs.fasta'
            print("Begin QUAST")
            subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/quast-5.0.2/quast.py '+assembly_result+' --min-contig 50 -o '+self.result_dir+'/identification/quast_out', shell=True, check=True)
            print("End QUAST")
        # else:
        #     assembly_obj.canu()
        #     assembly_result = self.result_dir+'/identification/assembly/canu_output/canu_assembly_result.contigs.fasta'


        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>assembly result is in %s</li>\n' % './identification/assembly')
        temp_file.write('<li><a href="%s">click to assembly result</a></li>\n' % ('./identification/assembly'))
        temp_file.write('<li>assembly qc result is in %s</li>\n' % './identification/quast_out')
        temp_file.write('<li><a href="%s">click to assembly qc result</a></li>\n' % ('./identification/quast_out/report.html'))
        temp_file.write('</ul>\n')
        temp_file.close()
        if assembly_conf['enable'] != False:
            blast_input = assembly_result
        else:
            scripts.fastq2fasta.fastq2fasta(self.input_file, self.result_dir+"/identification")
            blast_input = self.result_dir+"/identification/input.fasta"

        # scripts.fastq2fasta.fastq2fasta(self.input_file, self.result_dir+"/identification")
        
        # time.sleep(900)

        blastn_conf = self.conf['identification']['blastn']
        blastn_cline = NcbiblastnCommandline(cmd=os.path.dirname(os.path.realpath(__file__))+'/external_tools/blastn', query=blast_input, db=self.conf["identification"]['blastn']["blast_db_path"], outfmt=7, out=self.result_dir+"/identification/ncbi_fungi_blast_out.xml", evalue=1e-5)
        
        # blastn_cline.set_parameter('num_threads', int(blastn_conf['num_threads']))
        blastn_cline.set_parameter('num_threads', int(blastn_conf['num_threads']))
        blastn_cline.set_parameter('num_alignments', int(blastn_conf['num_alignments']))
        if blastn_conf['evalue'] != None:
            blastn_cline.set_parameter('evalue', blastn_conf['evalue'])
        # if blastn_conf['task'] != None:
        #     blastn_cline.set_parameter('task', blastn_conf['task'])
        if blastn_conf['penalty'] != None:
            blastn_cline.set_parameter('penalty', int(blastn_conf['penalty']))
        if blastn_conf['reward'] != None:
            blastn_cline.set_parameter('reward', int(blastn_conf['reward']))
        # if blastn_conf['dust'] != None:
        #     blastn_cline.set_parameter('dust', blastn_conf['dust'])
        # if blastn_conf['filtering_db'] != None:
        #     blastn_cline.set_parameter('filtering_db', blastn_conf['filtering_db'])
        # if blastn_conf['window_masker_taxid'] != None:
        #     blastn_cline.set_parameter('window_masker_taxid', blastn_conf['window_masker_taxid'])
        # if blastn_conf['no_greedy'] != None:
        #     blastn_cline.set_parameter('no_greedy', blastn_conf['no_greedy'])
        # if blastn_conf['min_raw_gapped_score'] != None:
        #     blastn_cline.set_parameter('min_raw_gapped_score', blastn_conf['min_raw_gapped_score'])
        # if blastn_conf['ungapped'] != None:
        #     blastn_cline.set_parameter('ungapped', blastn_conf['ungapped'])
        # if blastn_conf['off_diagonal_range'] != None:
        #     blastn_cline.set_parameter('off_diagonal_range', blastn_conf['off_diagonal_range'])
        print(blastn_cline)
        stdout, stderr = blastn_cline()
        print(stdout)
        print(stderr)

        accession_version_list = scripts.handle_blast_xml_result.handle_blast_xml_result_outfmt7(self.result_dir+"/identification/ncbi_fungi_blast_out.xml")
        accession_version_list = [accession_version_list[i][0] for i in range(int(self.conf["identification"]['number_of_candidate_similar_genome']))]
        # print("accession_version_list="+str(accession_version_list))

        for accession_version in accession_version_list:
            time.sleep(10)
            scripts.download_nucleotide.download_by_accession_version(self.result_dir, accession_version)

        genome_similarity_calculator = calculating_genome_similarity.GenomeSimilarityCalculator(self.result_dir, assembly_result, accession_version_list)
        closest_accession_version, max_jaccard = genome_similarity_calculator.search_similar_genome_from_bacteria_dataset()
        print("closest_accession_version = %s, max_jaccard = %s" % (closest_accession_version, max_jaccard))
        
        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>closest accession version is %s in %s Jaccard similarity coefficient</li>\n' % (closest_accession_version, max_jaccard))
        temp_file.write('</ul>\n')
        temp_file.close()

        # closest_accession_version = accession_version_list[0]
        # max_similarity = 0
        # for accession_version in accession_version_list:
        #     print(command_line % (accession_version, accession_version))
        #     subprocess.run(command_line % (accession_version, accession_version), shell=True, check=True)
        #     subprocess.run('samtools sort '+self.result_dir+'/identification/minimap2_'+accession_version+'_result.sam -o '+self.result_dir+'/identification/minimap2_'+accession_version+'_result.sorted.bam -O bam', shell=True, check=True)
        #     res = subprocess.Popen('bedtools genomecov -ibam '+self.result_dir+'/identification/minimap2_'+accession_version+'_result.sorted.bam', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        #     send_messages = res.stdout.readlines()
        #     print(send_messages[0].decode('utf-8'))
        #     for message in send_messages:
        #         message = message.decode('utf-8')
        #         if message.startswith('genome\t0'):
        #             print(message)
        #             line = message.split()
        #             if line[-1] == '\n':
        #                 new_similarity = 1 - float(line[-2])
        #             else:
        #                 new_similarity = 1 - float(line[-1])
        #             break
        #     print('new_similarity='+str(new_similarity))
        #     if new_similarity > max_similarity:
        #         max_similarity = new_similarity
        #         closest_accession_version = accession_version
        # print("closest_accession_version="+str(closest_accession_version))

        if self.conf['annotation']['cds_annotation']['enable'] != False:
            self.cds_annotation_3gs(closest_accession_version, assembly_result)

        if self.conf['annotation']['mlst'] != False:
            self.mlst(assembly_result)

        if self.conf['annotation']['prokka']['enable'] != False:
            scripts.prokka_annotation.annotation(assembly_result, self.result_dir, self.conf, closest_accession_version)


    def cds_annotation_ngs(self, closest_accession_version, assembly_result):
        print("begin cds annotation")
        alignment_tool = 'snap' if self.conf['annotation']["cds_annotation"]['alignment_tool']['snap'] != None else "bowtie2"
        if alignment_tool == 'bowtie2':
            subprocess.run('bowtie2-build '+self.result_dir+'/identification/'+closest_accession_version+'.fasta '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index', shell=True, check=True)
        else:
            subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/snap-aligner index '+self.result_dir+'/identification/'+closest_accession_version+'.fasta '+self.result_dir+'/identification/'+closest_accession_version+'_index', shell=True, check=True)
        if self.input_file_paired == None:
            assembly_conf = self.conf['identification']['assembly']
            if assembly_conf['enable'] != False:
                if alignment_tool == 'bowtie2':
                    subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -f -U '+assembly_result+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
                else:
                    scripts.fasta2fastq.fasta_to_fastq_by_biopython(assembly_result, self.result_dir)
                    assembly_result = self.result_dir+"/identification/assembly_result.fastq"
                    subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/snap-aligner single '+self.result_dir+'/identification/'+closest_accession_version+'_index '+assembly_result+' -o '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
            else:
                if alignment_tool == 'bowtie2':
                    subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -U '+self.input_file+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
                else:
                    subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/snap-aligner single '+self.result_dir+'/identification/'+closest_accession_version+'_index '+self.input_file+' -o '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
            # subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -U '+self.input_file+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
        else:
            assembly_conf = self.conf['identification']['assembly']
            if assembly_conf['enable'] != False:
                if alignment_tool == 'bowtie2':
                    subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -f -U '+assembly_result+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
                else:
                    scripts.fasta2fastq.fasta_to_fastq_by_biopython(assembly_result, self.result_dir)
                    assembly_result = self.result_dir+"/identification/assembly_result.fastq"
                    subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/snap-aligner single '+self.result_dir+'/identification/'+closest_accession_version+'_index '+assembly_result+' -o '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
            else:
                if alignment_tool == 'bowtie2':
                    subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -1 '+self.input_file+' -2 '+self.input_file_paired+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
                else:
                    subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/snap-aligner paired '+self.result_dir+'/identification/'+closest_accession_version+'_index '+self.input_file+' '+self.input_file_paired+' -o '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)
            # subprocess.run('bowtie2 -x '+self.result_dir+'/identification/'+closest_accession_version+'_bowtie2_index -1 '+self.input_file+' -2 '+self.input_file_paired+' -S '+self.result_dir+'/identification/alignment_result.sam', shell=True, check=True)

        print("begin sort_sam")
        subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/samtools-1.10/samtools view -bS '+self.result_dir+'/identification/alignment_result.sam > '+self.result_dir+'/identification/output.bam', shell=True, check=True)
        subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/samtools-1.10/samtools sort '+self.result_dir+'/identification/output.bam -o '+self.result_dir+'/identification/alignment_result.sorted.sam -O sam', shell=True, check=True)
        print("end sort_sam")

        scripts.download_gb.download_by_accession_version(self.result_dir, closest_accession_version)
        # subprocess.run('perl scripts/download_genbank.pl '+closest_accession_version+' '+self.result_dir+'/identification', shell=True, check=True)
        transform = scripts.genbank2gff3.Genbank2gff3(closest_accession_version+'.gb', self.result_dir)
        # transform.genbank2gff3_by_bioperl()
        transform.genbank2gff3_by_bcbio()

        annotaion_generator = scripts.annotation_generator.Annotation_generator(self.result_dir+'/identification/alignment_result.sorted.sam', self.result_dir+'/identification/'+closest_accession_version+'.gff', self.result_dir)
        annotaion_generator.look_for_annotation()
        print("end cds annotation")


    def cds_annotation_3gs(self, closest_accession_version, assembly_result):
        print("begin cds annotation")

        # minimap2
        minimap2_conf = self.conf['annotation']['cds_annotation']['alignment_tool']['minimap2']
        command_line = "minimap2 -a "
        if minimap2_conf['-H'] != None:
            command_line += "-H "
        if minimap2_conf['-k'] != None:
            command_line += "-k "+str(minimap2_conf['-k'])+' '
        if minimap2_conf['-w'] != None:
            command_line += "-w "+str(minimap2_conf['-w'])+' '
        if minimap2_conf['-I'] != None:
            command_line += "-I "+str(minimap2_conf['-I'])+' '
        if minimap2_conf['-f'] != None:
            command_line += "-f "+str(minimap2_conf['-f'])+' '
        if minimap2_conf['-g'] != None:
            command_line += "-g "+str(minimap2_conf['-g'])+' '
        if minimap2_conf['-G'] != None:
            command_line += "-G "+str(minimap2_conf['-G'])+' '
        if minimap2_conf['-F'] != None:
            command_line += "-F "+str(minimap2_conf['-F'])+' '
        if minimap2_conf['-r'] != None:
            command_line += "-r "+str(minimap2_conf['-r'])+' '
        if minimap2_conf['-n'] != None:
            command_line += "-n "+str(minimap2_conf['-n'])+' '
        if minimap2_conf['-m'] != None:
            command_line += "-m "+str(minimap2_conf['-m'])+' '
        if minimap2_conf['-X'] != None:
            command_line += "-X "
        if minimap2_conf['-p'] != None:
            command_line += "-p "+str(minimap2_conf['-p'])+' '
        if minimap2_conf['-N'] != None:
            command_line += "-N "+str(minimap2_conf['-N'])+' '
        if minimap2_conf['-A'] != None:
            command_line += "-A "+str(minimap2_conf['-A'])+' '
        if minimap2_conf['-B'] != None:
            command_line += "-B "+str(minimap2_conf['-B'])+' '
        if minimap2_conf['-O'] != None:
            command_line += "-O "+str(minimap2_conf['-O'])+' '
        if minimap2_conf['-E'] != None:
            command_line += "-E "+str(minimap2_conf['-E'])+' '
        if minimap2_conf['-z'] != None:
            command_line += "-z "+str(minimap2_conf['-z'])+' '
        if minimap2_conf['-s'] != None:
            command_line += "-s "+str(minimap2_conf['-s'])+' '
        if minimap2_conf['-u'] != None:
            command_line += "-u "+str(minimap2_conf['-u'])+' '
        if minimap2_conf['-x'] != None:
            command_line += "-x "+str(minimap2_conf['-x'])+' '
        command_line += self.result_dir+"/identification/%s.fasta "+assembly_result+" > "+self.result_dir+"/identification/minimap2_%s_result.sam"

        subprocess.run(command_line % (closest_accession_version, closest_accession_version), shell=True, check=True)

        print("begin sort_sam")
        subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/samtools-1.10/samtools sort '+self.result_dir+'/identification/minimap2_'+closest_accession_version+'_result.sam -o '+self.result_dir+'/identification/minimap2_'+closest_accession_version+'_result.sorted.sam -O sam', shell=True, check=True)
        print("end sort_sam")
        
        scripts.download_gb.download_by_accession_version(self.result_dir, closest_accession_version)
        # subprocess.run('perl scripts/download_genbank.pl '+closest_accession_version+' '+self.result_dir+'/identification', shell=True, check=True)
        transform = scripts.genbank2gff3.Genbank2gff3(closest_accession_version+'.gb', self.result_dir)
        # transform.genbank2gff3_by_bioperl()
        transform.genbank2gff3_by_bcbio()

        annotaion_generator = scripts.annotation_generator.Annotation_generator(self.result_dir+'/identification/minimap2_'+closest_accession_version+'_result.sorted.sam', self.result_dir+'/identification/'+closest_accession_version+'.gff', self.result_dir)
        annotaion_generator.look_for_annotation()
        print("end cds annotation")
        
        
        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>cds annotation result is %s</li>\n' % './annotation/cds_annotation')
        temp_file.write('<li><a href="%s">click to cds annotation result</a></li>\n' % ('./annotation/cds_annotation'))
        temp_file.write('</ul>\n')
        temp_file.close()


    

    def mlst(self, contigs):
        print('begin mlst ngs')
        os.mkdir(self.result_dir+'/mlst')
        subprocess.run(os.path.dirname(os.path.realpath(__file__))+'/external_tools/mlst/bin/mlst '+contigs+' --json '+self.result_dir+'/mlst/mlst_result.json', shell=True, check=True)
        print('end mlst ngs')

        
        temp_file = open(os.path.abspath('.') + '/' + self.result_dir+'/Summary_of_results.html', 'a+')
        temp_file.write('<ul>\n')
        temp_file.write('<li>mlst result is %s</li>\n' % './mlst/')
        temp_file.write('<li><a href="%s">click to mlst result</a></li>\n' % ('./mlst/'))
        temp_file.write('</ul>\n')
        temp_file.close()
