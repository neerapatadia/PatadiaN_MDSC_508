"""
Project: MDSC 508 Thesis
Author: Neera Patadia

Description:
This script is used to organize the MAF files obtained from Firhose into the
format for the CBaSE algorithm as layed out by Weghorn et al. for subclonal variants.

Input File:
SKCM Mutation Anotation Files (MAF) obtained from Firehose: http://firebrowse.org/.

Output File:
Formated MAF file with gene name (HNGC symbol), mutation effect, alternate
nucleotide, and tri-nucleotide context

Running Instructions:
ulimit -n 5000
python3 SKCM_vaf_change_bayesian.py
"""
import os
import re

SKCM_maf_files = []
for i in os.listdir("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/MAF_Files/SKCM_cancer_mafs"):
    if i.endswith("maf.txt"):
        SKCM_maf_files.append(open("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/MAF_Files/SKCM_cancer_mafs/"+i, "r", encoding="ISO-8859-1"))
        print(i)

context_map = open("/Users/Neera/Dropbox (APJdKL)/Patadia-Neera/Working/MAF_Files/context_map.txt", "r")
counting_variants_subclonal = open("counting_subclonal_variants.txt", "+w")
counting_variants_subclonal.write("Cancer Type" + "\t" + "Number of Variants" + "\n")


SKCM_maf_reassembly = open("SKCM_maf_subclonal_bayesian.txt", "+w")
SKCM_maf_reassembly.write("Gene" + "\t" + "mut_eff" + "\t" + "mut_nuc" + "\t" + "context" + "\n")

context_num = []
context_tri = []
count_clonal_skcm = 0
for file in SKCM_maf_files:
    count = 0
    for line in file:
        count +=1
        if count != 1:
            header = line.split("\t")
            if header[9] == "SNP": #only include SNPs in analysis
                # calculate variant allele frequency
                VAF = int(header[83])/(int(header[83]) + int(header[80]))
                if VAF < 0.5:
                    print("fixed")
                    if ">" in header[40]:
                        codon_change = header[40].split(")")
                        codon_change = codon_change[1].split(">")
                        codon_value = codon_change[0]

                        for elem in context_map:
                            context_value = elem.split()
                            context_num.append(context_value[0])
                            context_tri.append(context_value[2])

                        for tri in range(len(context_tri)- 1):
                            if codon_value.upper() == context_tri[tri].upper():
                                context = context_num[tri]

                    if header[8] == "Silent":
                        header[8] = "coding-synon"
                        count_clonal_skcm += 1
                        SKCM_maf_reassembly.write(header[0] + "\t" + header[8] + "\t" + header[12] + "\t" + context +"\n")
                    elif header[8] == "Missense_Mutation":
                        header[8] = "missense"
                        count_clonal_skcm += 1
                        SKCM_maf_reassembly.write(header[0] + "\t" + header[8] + "\t" + header[12] + "\t" + context +"\n")
                    elif header[8] == "Nonsense_Mutation":
                        header[8] = "nonsense"
                        count_clonal_skcm += 1
                        SKCM_maf_reassembly.write(header[0] + "\t" + header[8] + "\t" + header[12] + "\t" + context +"\n")
                    else:
                        print("Note missense, nonsense or silent, so will not write to file")
