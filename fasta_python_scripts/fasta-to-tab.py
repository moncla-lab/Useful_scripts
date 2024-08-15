#!/usr/bin/python


# Lambodhar Damdoaran
# Script to convert tab file to fasta


from Bio import SeqIO

data = input("Enter fasta file: ")

rec = SeqIO.parse(data, "fasta")
write = SeqIO.write(rec, "output.tsv","tab")


