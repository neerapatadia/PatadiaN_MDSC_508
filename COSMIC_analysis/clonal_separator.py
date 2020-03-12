"""
Project: MDSC 508 Thesis
Author: Neera Patadia

Description:
This script was used to separate

Input File:
list of clonal variants.

Output File:
set of subclonal variants with 10 000 variants per file.

Running Instructions:
python3 clonal_separator.py
"""
import os

clonal_variants = open("skcm_clonal_variants.txt", "r")

clonal1 = open("skcm_clonal_vars_1.txt", "w")
clonal2 = open("skcm_clonal_vars_2.txt", "w")
clonal3 = open("skcm_clonal_vars_3.txt", "w")
clonal4 = open("skcm_clonal_vars_4.txt", "w")

clonal1.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
clonal2.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
clonal3.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
clonal4.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")

count = 0
for line in clonal_variants:
    count += 1
    if count == 0:
        clonal1.write(line + "\n")
        clonal2.write(line + "\n")
        clonal3.write(line + "\n")
        clonal4.write(line + "\n")
    elif 1 <= count and count <= 10000:
        clonal1.write(line + "\n")
    elif 10000 < count and count <= 20000:
        clonal2.write(line + "\n")
    elif 20000 < count and count <= 30000:
        clonal3.write(line + "\n")
    elif 30000 < count:
        clonal4.write(line + "\n")
    else:
        print("yeet")

clonal_variants.close()
clonal1.close()
clonal2.close()
clonal3.close()
clonal4.close()
