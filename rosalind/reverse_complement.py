# This program calculates the reverse complement of a DNA sequence

import sys

complement = {
'A':'T',
'T':'A',
'G':'C',
'C':'G'
}

def reverse_complement(dna):
	'''
	This function recives a DNA string and returns its reverse complement
	'''
	reverse_dna = dna[::-1]
	reverse_complement = ''
	for i in reverse_dna:
		reverse_complement += complement[i]

	return reverse_complement

if __name__ == "__main__":
	# Take input from user
	dna = input("Type DNA sequence:")
	print(f"Reverse complement: {reverse_complement(dna)}")
