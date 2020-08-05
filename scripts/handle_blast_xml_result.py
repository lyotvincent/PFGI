import os
import sys
from Bio import SearchIO

def handle_blast_xml_result(filename):
    print('begin handle_blast_xml_result')
    accession_version_dict = {}
    # if os.path.isfile(filename):
    #     print("Handling...")
    #     blast_qresult = SearchIO.parse(filename, "blast-xml")
    #     for hit in blast_qresult:
    #         print(str(hit.id))
    #         accession_version = str(hit.id).split('|')[1]
    #         if accession_version in accession_version_dict:
    #             accession_version_dict[accession_version] += 1
    #         else:
    #             accession_version_dict[accession_version] = 1
    #     print("Handled")
    blast_result = open(filename, 'r')
    line = blast_result.readline()
    while line:
        if '<Hit_id>' in line and '</Hit_id>' in line:
            accession_version = str(line).split('|')[1]
            if accession_version in accession_version_dict:
                accession_version_dict[accession_version] += 1
            else:
                accession_version_dict[accession_version] = 1
        line = blast_result.readline()
    blast_result.close()
    print('end handle_blast_xml_result')
    return sorted(accession_version_dict.items(), key=lambda d: d[1], reverse=True)

def handle_blast_xml_result_outfmt7(filename):
    blast_result_file = open(filename, 'r')
    blast_lines = blast_result_file.readlines()
    blast_result_file.close()

    accession_version_dict = {}

    for blast_line in blast_lines:
        if not blast_line.startswith('#'):
            # items[1] = subject acc.ver; items[2] = % identity; items[3] = alignment length
            items = blast_line.split()
            items[2] = float(items[2])
            items[3] = float(items[3])
            if not accession_version_dict.__contains__(items[1]):
                accession_version_dict[items[1]] = items[2]*0.01*items[3]
            else:
                accession_version_dict[items[1]] += items[2]*0.01*items[3]

    accession_version_list = []
    for key in accession_version_dict:
        # map_identification_list.append([key, family_weight_dict[key][0] / family_weight_dict[key][1]])
        accession_version_list.append([key, accession_version_dict[key]])

    accession_version_list = sorted(accession_version_list, key=lambda x:x[1], reverse=True)
    print(accession_version_list[:50])
    return accession_version_list

# def handle_blast_xml_result(filename):
#     if not os.path.isfile(filename):
#         gi_dict = {}
#         print("Handling...")
#         blast_qresult = SearchIO.read(filename, "blast-xml")
#         for hit in blast_qresult:
#             gi = str(hit.id).split('|')[1]
#             if gi in gi_dict:
#                 gi_dict[gi] += 1
#             else:
#                 gi_dict[gi] = 1
#         print("Handled")
#     return sorted(gi_dict.items(), key=lambda d: d[1], reverse=True)

# def handle_blast_xml_result():
#     argv = sys.argv
#     filename = argv[1]
#     if not os.path.isfile(filename):
#         gi_dict = {}
#         print("Handling...")
#         blast_qresult = SearchIO.read(filename, "blast-xml")
#         for hit in blast_qresult:
#             gi = str(hit.id).split('|')[1]
#             if gi in gi_dict:
#                 gi_dict[gi] += 1
#             else:
#                 gi_dict[gi] = 1
#         print("Handled")
#     return sorted(gi_dict.items(), key=lambda d: d[1], reversed=True) # [("a", 4), ("b", 2), ("c", 1)]

# if __name__ == "__main__":
#     handle_blast_xml_result()
