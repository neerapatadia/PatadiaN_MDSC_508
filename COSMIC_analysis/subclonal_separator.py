"""
Project: MDSC 508 Thesis
Author: Neera Patadia

Description:
This script was used to separate

Input File:
list of subclonal variants.

Output File:
set of subclonal variants with 10 000 variants per file.

Running Instructions:
python3 subclonal_separator.py
"""
import os

subclonal_variants = open("skcm_subclonal_variants.txt", "r")

subclonal1 = open("skcm_subclonal_vars_1.txt", "w")
subclonal2 = open("skcm_subclonal_vars_2.txt", "w")
subclonal3 = open("skcm_subclonal_vars_3.txt", "w")
subclonal4 = open("skcm_subclonal_vars_4.txt", "w")
subclonal5 = open("skcm_subclonal_vars_5.txt", "w")
subclonal6 = open("skcm_subclonal_vars_6.txt", "w")
subclonal7 = open("skcm_subclonal_vars_7.txt", "w")
subclonal8 = open("skcm_subclonal_vars_8.txt", "w")
subclonal9 = open("skcm_subclonal_vars_9.txt", "w")
subclonal10 = open("skcm_subclonal_vars_10.txt", "w")
subclonal11 = open("skcm_subclonal_vars_11.txt", "w")
subclonal12 = open("skcm_subclonal_vars_12.txt", "w")
subclonal13 = open("skcm_subclonal_vars_13.txt", "w")
subclonal14 = open("skcm_subclonal_vars_14.txt", "w")
subclonal15 = open("skcm_subclonal_vars_15.txt", "w")
subclonal16 = open("skcm_subclonal_vars_16.txt", "w")
subclonal17 = open("skcm_subclonal_vars_17.txt", "w")
subclonal18 = open("skcm_subclonal_vars_18.txt", "w")
subclonal19 = open("skcm_subclonal_vars_19.txt", "w")
subclonal20 = open("skcm_subclonal_vars_20.txt", "w")
subclonal21 = open("skcm_subclonal_vars_21.txt", "w")
subclonal22 = open("skcm_subclonal_vars_22.txt", "w")
subclonal23 = open("skcm_subclonal_vars_23.txt", "w")
subclonal24 = open("skcm_subclonal_vars_24.txt", "w")
subclonal25 = open("skcm_subclonal_vars_25.txt", "w")
subclonal26 = open("skcm_subclonal_vars_26.txt", "w")


subclonal1.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal2.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal3.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal4.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal5.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal6.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal7.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal8.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal9.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal10.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal11.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal12.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal13.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal14.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal15.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal16.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal17.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal18.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal19.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal20.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal21.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal22.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal23.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal24.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal25.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")
subclonal26.write("Gene" + "\t" + "mut_eff" + "\t" + "cDNA_change" + "\t" + "Ref" + "\t" + "Alt" +"\n")

count = 0
for line in subclonal_variants:
    count += 1
    if count == 0:
        subclonal1.write(line )
        subclonal2.write(line )
        subclonal3.write(line )
        subclonal4.write(line )
        subclonal5.write(line )
        subclonal6.write(line )
        subclonal7.write(line )
        subclonal8.write(line )
        subclonal9.write(line )
        subclonal10.write(line )
        subclonal11.write(line )
        subclonal12.write(line )
        subclonal13.write(line )
        subclonal14.write(line )
        subclonal15.write(line )
        subclonal16.write(line )
        subclonal17.write(line )
        subclonal18.write(line )
        subclonal19.write(line )
        subclonal20.write(line )
        subclonal21.write(line )
        subclonal22.write(line )
        subclonal23.write(line )
        subclonal24.write(line )
        subclonal25.write(line )
        subclonal26.write(line )

    elif 1 <= count and count <= 10000:
        subclonal1.write(line)
    elif 10000 < count and count <= 20000:
        subclonal2.write(line )
    elif 20000 < count and count <= 30000:
        subclonal3.write(line )
    elif 30000 < count and count <= 40000:
        subclonal4.write(line )
    elif 40000 < count and count <= 50000:
        subclonal5.write(line)
    elif 50000 < count and count <= 60000:
        subclonal6.write(line )
    elif 60000 < count and count <= 70000:
        subclonal7.write(line )
    elif 70000 < count and count <= 80000:
        subclonal8.write(line )
    elif 80000 < count and count <= 90000:
        subclonal9.write(line)
    elif 90000 < count and count <= 100000:
        subclonal10.write(line )
    elif 100000 < count and count <= 110000:
        subclonal11.write(line )
    elif 110000 < count and count <= 120000:
        subclonal12.write(line )
    elif 120000 < count and count <= 130000:
        subclonal13.write(line)
    elif 130000 < count and count <= 140000:
        subclonal14.write(line )
    elif 140000 < count and count <= 150000:
        subclonal15.write(line )
    elif 150000 < count and count <= 160000:
        subclonal16.write(line )
    elif 160000 < count and count <= 170000:
        subclonal17.write(line)
    elif 170000 < count and count <= 180000:
        subclonal18.write(line )
    elif 180000 < count and count <= 190000:
        subclonal19.write(line )
    elif 190000 < count and count <= 200000:
        subclonal20.write(line )
    elif  200000 < count and count <= 210000:
        subclonal21.write(line)
    elif 210000 < count and count <= 220000:
        subclonal22.write(line )
    elif 220000 < count and count <= 230000:
        subclonal23.write(line )
    elif 230000 < count and count <= 240000:
        subclonal24.write(line )
    elif 240000 < count and count <= 250000:
        subclonal25.write(line )
    elif 250000 < count:
        subclonal26.write(line )
    else:
        print(count)



subclonal_variants.close()
subclonal1.close()
subclonal2.close()
subclonal3.close()
subclonal4.close()
subclonal5.close()
subclonal6.close()
subclonal7.close()
subclonal8.close()
subclonal9.close()
subclonal10.close()
subclonal11.close()
subclonal12.close()
subclonal13.close()
subclonal14.close()
subclonal15.close()
subclonal16.close()
subclonal17.close()
subclonal18.close()
subclonal19.close()
subclonal20.close()
subclonal21.close()
subclonal22.close()
subclonal23.close()
subclonal24.close()
subclonal25.close()
subclonal26.close()
