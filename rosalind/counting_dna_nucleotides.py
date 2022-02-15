# This program reads a DNA sequence and prints the absolute frequency of each nucleotide

import sys

# Take input from user
dna = input("Type DNA sequence:")

for i in 'ACGT':
	print(f"{i} : {dna.count(i)}")