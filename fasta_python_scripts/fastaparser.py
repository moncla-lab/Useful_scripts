# Lambodhar Damodaran
# Parse large FASTA file for subset list in text file
# Usage  python fastaparser.py input_file id_file output_file

from Bio import SeqIO
import sys


input_file = SeqIO.parse(sys.argv[1], "fasta")
id_file = set(line.strip() for line in open(sys.argv[2]))
output_file = sys.argv[3]

records = (r for r in input_file if r.id in id_file)
count = SeqIO.write(records, output_file, "fasta")
print("Saved %i records from %s to %s" % (count, input_file, output_file))
if count < len(id_file):
    print("Warning %i IDs not found in %s" % (len(id_file) - count, input_file))