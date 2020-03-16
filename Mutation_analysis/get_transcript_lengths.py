"""
Project: MDSC 508 Thesis 
Author: Neera Patadia 

Description: 
This script is used to get the lengths for an inputed gene list 
The input gene list is checked agains the biomart_export database 
to get the start and end positions. Gene Length is calculated by 
taking the end position - start postion of a given gene. The output
From this file is used as the input for the computation of normalized
gene counts.

Input File: 
List of genes (HNGC symbols) with the number of mutations on the gene.
Number of mutations found on gene taken from the COSMIC database. 

Output File: 
List of genes with HNGC symbol, start position, end position, 
calculated length and the number of mutations found on gene. 

Running Instructions:
python3 get_transcript_lengths.py  <input_gene_list_name> <output_gene_list_name> 
"""

import os
import sys

input_gene_list = sys.argv[1]
output_gene_list = sys.argv[2]
# input gene list should have information on gene and frequency


biomart = open("biomart_export.txt", "r")
gene_list = open(input_gene_list, "r")
gene_lengths = open(output_gene_list, "w")

gene_lengths.write("Gene_Name" + "\t" + "Start" + "\t" + "End" + "\t" + "Length" + "\t" + "Frequency" + "\n")



count = 0
for line in gene_list:
    count += 1
    gene_headers = line.split("\t")
    if count > 1:
        gene_name = gene_headers[0]
        count2 = 0
        biomart.seek(0, 0)
        for row in biomart:

            biomart_headers = row.split("\t")
            bio_gene_name = biomart_headers[3]
            count2 += 1


            if count2 > 1:
                print(bio_gene_name + "\t" + gene_name + "\n")
                if bio_gene_name == gene_name:
                    start_pos = int(biomart_headers[1])
                    end_pos = int(biomart_headers[2])
                    length = end_pos - start_pos


                    gene_lengths.write(gene_name + "\t" + str(start_pos) + "\t" + str(end_pos) + "\t" + str(length) + "\t" + gene_headers[1] + "\n")
            gene_lengths.flush()

biomart.close()
gene_list.close()
gene_lengths.close()
