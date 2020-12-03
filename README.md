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
## External tools
These software/tools respectively support part of the entire pipeline. If you want to use all the functions of the pipeline, all these software in the table should be installed.  
The ✔ in 'conda' column means that the software cound install by conda.  

|software|conda|download link|
|----|----|----|
|FastQC|✔|<http://www.bioinformatics.babraham.ac.uk/projects/fastqc/>|
|fastp|✔|<https://github.com/OpenGene/fastp>|
|trimmomatic|✔|<https://github.com/timflutre/trimmomatic>|
|cutadapt|✔|<https://github.com/marcelm/cutadapt>|
|megahit|✔|<https://github.com/voutcn/megahit>|
|spades|✔|<https://github.com/ablab/spades>|
|velvet|✔|<https://github.com/dzerbino/velvet>|
|QUAST|✔|<https://github.com/ablab/quast>|
|BLAST|✔|<https://blast.ncbi.nlm.nih.gov/Blast.cgi>|
|prokka|✔|<https://github.com/tseemann/prokka>|
|prodigal|✔|<https://github.com/hyattpd/Prodigal>|
|snap-aligner|✔|<https://github.com/amplab/snap>|
|bowtie2|✔|<https://github.com/BenLangmead/bowtie2>|
|samtools|✔|<https://github.com/samtools/samtools>|
|bedtools|✔|<https://github.com/arq5x/bedtools2>|
|minimap2|✔|<https://github.com/lh3/minimap2>|
|biopython|✔|pip
|bcbio-gff|✔|pip
