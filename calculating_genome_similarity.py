from datasketch import MinHash
import glob

class GenomeSimilarityCalculator:

    def __init__(self, result_dir, contigs_path, accession_version_list):
        self.__result_dir = result_dir
        self.__contigs_path = contigs_path
        self.__accession_version_list = accession_version_list
        self.__k_mer_length = 15
        super().__init__()

    def _get_sequence_from_fasta(self, fasta_file_name):
        temp_file = open(fasta_file_name, 'r')
        lines = temp_file.readlines()
        temp_file.close()

        sequence = ''
        accession = ''
        for line in lines:
            if line.startswith(">"):
                if sequence != '':
                    print('there are many sequences in a fna file.')
                    break
                accession = line[1:].strip()
                continue
            else:
                sequence += line.strip()

        return accession, sequence

    # 用一条输入DNA序列构建MinHash
    def _construct_minhash(self, sequence):
        temp_minhash = MinHash(num_perm=2048)

        for i in range( len(sequence)-self.__k_mer_length+1 ):
            temp_minhash.update(sequence[i:i+self.__k_mer_length].encode('utf8'))
        
        return temp_minhash

    def _construct_contigs_minhash(self):
        print('begin_construct_contigs_minhash')
        
        contigs_minhash = MinHash(num_perm=2048)

        contigs_file = open(self.__contigs_path, 'r')
        contigs_lines = contigs_file.readlines()
        contigs_file.close()
        for contig in contigs_lines:
            if contig.startswith('>'):
                continue
            contigs_minhash.merge(self._construct_minhash(contig.strip()))
        
        print('end_construct_contigs_minhash')
        return contigs_minhash

    def search_similar_genome_from_bacteria_dataset(self):

        max_jaccard = 0
        closest_genome = ''

        contigs_minhash = self._construct_contigs_minhash()

        for accession_version in self.__accession_version_list:
            accession, refseq = self._get_sequence_from_fasta(self.__result_dir+'/identification/'+accession_version+'.fasta')
            print('calculate %s' % accession)
            refseq_minhash = self._construct_minhash(refseq)

            # 然后用contigs输入minhash，再比较
            temp_jaccard = contigs_minhash.jaccard(refseq_minhash)
            print(accession_version+' jaccard = '+str(temp_jaccard))

            if temp_jaccard > max_jaccard:
                closest_genome = accession_version
                max_jaccard = temp_jaccard
        
        return closest_genome, max_jaccard

# data1 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for', 'estimating', 'the', 'similarity', 'between', 'datasets']
# data2 = ['minhash', 'is', 'a', 'probability', 'data', 'structure', 'for', 'estimating', 'the', 'similarity', 'between', 'documents']
# data3 = ['minhash', 'is', 'a', 'probabilistic', 'data', 'structure', 'for']
# data4 = ['estimating', 'the', 'similarity', 'between', 'datasets']

# m1, m2 = MinHash(), MinHash()
# for d in data1:
#     m1.update(d.encode('utf8'))
# for d in data2:
#     m2.update(d.encode('utf8'))
# print("Estimated Jaccard for data1 and data2 is", m1.jaccard(m2))

# m3, m4 = MinHash(), MinHash()
# for d in data3:
#     m3.update(d.encode('utf8'))
# for d in data4:
#     m4.update(d.encode('utf8'))

# m3.merge(m4)
# print("Estimated Jaccard for data3 and data2 is", m3.jaccard(m2))


# s1 = set(data1)
# s2 = set(data2)
# actual_jaccard = float(len(s1.intersection(s2)))/float(len(s1.union(s2)))
# print("Actual Jaccard for data1 and data2 is", actual_jaccard)
