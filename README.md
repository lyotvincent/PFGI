[TOC]
# PFGI
## introduce
PFGI is a bioinformatics pipeline for fungal genome identification and annotation.
## How to use the tool
1. Download: clone from github: git clone https://github.com/lyotvincent/OntoVarSearch.git
2. Configuration file: User could set software parameters in pfgi_configuration_template.xlsx and use "-conf_file_path pfgi_configuration.xlsx" to let program know where the configuration file is.
3. Download fungal genomes & build database. `python download_fungi_data.py`. Next, the database path should be written in the configuration file.
4. run this command to get 'help': python fungi_pipeline.py -h  
help information:  
-f&emsp;#input single end file (fastq format)  
-1 and -2&emsp;#input paired end files (fastq format)  
-ngs or -3gs&emsp;#choose which mode to run (Required)  
-conf_file_path&emsp;#the configuration file path (Required)  
-o&emsp;#out directory name  
-h or -help or --h or --help&emsp;#get help information  
a example:  
`python ../PFGI/fungi_pipeline.py -1 SRR7530142_1.fastq -2 SRR7530142_2.fastq -ngs -conf_file_path ../PFGI/pfgi_configuration_template.xlsx -o SRR7530142`
