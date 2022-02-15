# This program converts a DNA sequence (ATCG) to RNA sequence (AUCG)

import sys

def dna_to_rna(dna):
	'''
	This function convert dna sequence to rna sequence
	input: String of DNA (ATCG)
	output: String of RNA (AUCG)
	'''
	rna = dna.replace('T', 'U', len(dna))
	return rna

if __name__ == "__main__":
	# Take input from user
	dna = input("Type DNA sequence:")
	print(f"RNA sequence: {dna_to_rna(dna)}")