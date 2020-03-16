"""
Project: MDSC 508 Thesis
Author: Neera Patadia

Description:
This script is used to remove oncogenes from the cosmic database.

Input File:
Cosmic db file and list of oncogenes

Output File:
Cosmic db with no oncogene records

Running Instructions:
python3 cosmic_parsing.py
"""
import os

cosmic_db = open("V90_37_MUTANT.csv", "r")
oncogene_list = open("ongene_human.txt", "r")
cosmic_db_filtered = open("Cosmic_no_onco_skin.csv", "w")

oncogenes = []

count = 0
for line in cosmic_db:
    count += 1
    header = line.split(",")
    if count == 1:
        cosmic_db_filtered.write(line + "\n")
    if count > 1:
        #oncogene_list.seek(0, 0)
        for element in oncogene_list:
            header_onco = element.split("\t")
            oncogenes.append(header_onco[1])

        if header[0] not in oncogenes:
            cosmic_db_filtered.write(line + "\n")
        #cosmic_db_filtered.flush()

cosmic_db.close()
oncogene_list.close()
