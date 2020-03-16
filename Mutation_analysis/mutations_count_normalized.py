"""
Project: MDSC 508 Thesis 
Author: Neera Patadia

Description: 
This script is used to determine the normalized mutation count 
on a list of genes. Normalization is calculated by taking the 
number of reported mutations on the gene, and dividing it by 
the length of the gene (where length of gene was calculated 
using get_transcript_length.py). Output consists of gene names 
(HNGC symbols) and the normalized mutation count. 

Input File: 
List of genes (HNGC symbols) with the number of mutations on the gene.
Number of mutations found on gene taken from the COSMIC database. Please 
note that the header parameters may need to be modified based on the 
format of the input file. Input should be a tab-deliminated file.

Output File: 
List of genes with HNGC symbol and the normalized gene counts. Output
is a tab-deliminated file.

Running Instructions:
python3 mutation_count_normalized.py <input_file_name> <output_file_name>

"""
import os
import sys

input_gene_lengths = sys.argv[1]
output_gene_lengths_normalized = sys.argv[2]

gene_lens = open(input_gene_lengths, "r")
gene_lens_normalized = open(output_gene_lengths_normalized, "w")

gene_lens_normalized.write("Gene" + "\t" + "Normalized_Count" + "\n")

count = 0
for line in gene_lens:
    count += 1
    gene_lens_headers = line.split("\t")
    if count > 1:
        if len(gene_lens_headers) != 1:
            gene_name = gene_lens_headers[0]
            count = int(gene_lens_headers[4])
            lengths = int(gene_lens_headers[3])
            normalized_count = count/lengths

            gene_lens_normalized.write(gene_name + "\t" + str(normalized_count) + "\n")
