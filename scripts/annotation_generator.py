import os
import sys
import subprocess

class Annotation_generator:

    sam_file = ''
    gff_file = ''
    result_dir = None

    def __init__(self, sam, gff, result_dir):
        self.sam_file = sam
        self.gff_file = gff
        self.result_dir = result_dir
    
    def look_for_annotation(self):
        print("begin look_for_annotation")
        
        sam_reader = open(self.sam_file, 'r')
        gff_reader = open(self.gff_file, 'r')
        os.mkdir(self.result_dir+'/annotation')
        result_writer = open(self.result_dir+'/annotation/cds_annotation', 'w', encoding='utf-8')

        # sam_line = sam_reader.readline()
        # while "@" == sam_line[0]:
        #     sam_line = sam_reader.readline()

        # gff_line = gff_reader.readline()
        # while "#" == gff_line[0]:
        #     gff_line = gff_reader.readline()

        # sam_lines = sam_reader.readlines()
        # gff_lines = gff_reader.readlines()

        # result_writer.write('# sam file info\n')
        # sam_line = sam_lines[0]
        # while "@" == sam_line[0]:
        #     result_writer.write(sam_line)
        #     sam_lines.remove(sam_line)
        #     sam_line = sam_lines[0]
        
        result_writer.write('# sam file info\n')
        sam_line = sam_reader.readline()
        while sam_line.startswith('@'):
            result_writer.write(sam_line)
            sam_line = sam_reader.readline()
        
        # result_writer.write('# gff file info\n')
        # gff_line = gff_lines[0]
        # while "#" == gff_line[0]:
        #     result_writer.write(gff_line)
        #     gff_lines.remove(gff_line)
        #     gff_line = gff_lines[0]

        result_writer.write('# gff file info\n')
        gff_line = gff_reader.readline()
        while gff_line.startswith('#'):
            result_writer.write(gff_line)
            gff_line = gff_reader.readline()

        while sam_line:
            sam_line_list = sam_line.split('\t')
            # print(sam_line_list)
            sam_line_begin = int(sam_line_list[3])
            sam_line_end = sam_line_begin+len(sam_line_list[9])
            # print('sam_line_begin='+str(sam_line_begin)+' end='+str(sam_line_end))
            if sam_line_begin == 0: # not align to the reference genome
                break
            while gff_line:
                gff_line_list = gff_line.split('\t')
                # print(gff_line_list)
                gff_line_begin = int(gff_line_list[3])
                gff_line_end =  gff_line_begin + int(gff_line_list[4]) - int(gff_line_list[3]) + 1
                # print("gff_line_begin="+str(gff_line_begin)+' gff_line_end='+str(gff_line_end))
                if sam_line_begin <= gff_line_begin and sam_line_end >= gff_line_end:
                    result_writer.write(gff_line)
                elif sam_line_end < gff_line_begin:
                    break
                gff_line = gff_reader.readline()
            sam_line = sam_reader.readline()

        sam_reader.close()
        gff_reader.close()
        result_writer.close()
        print("end look_for_annotation")

# def main():
#     argv = sys.argv
#     sam, gff = argv[1], argv[2]    
#     sort = annotation_generator(sam, gff)
#     sort.look_for_annotation()

# if __name__ == "__main__":
#     main()