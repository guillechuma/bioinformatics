# This Python file uses the following encoding: utf-8
import sys

# Data stricture for the genetic code
rna_codon = {'UUU' : 'F',
			'UUC' : 'F',
			'UUA' : 'L',
			'UUG' : 'L',
			'UCU' : 'S',
			'UCC' : 'S',
			'UCA' : 'S',
			'UCG' : 'S',
			'UAU' : 'Y',
			'UAC' : 'Y',
			'UAA' : -1,
			'UAG' : -1,
			'UGU' : 'C',
			'UGC' : 'C',
			'UGA' : -1,
			'UGG' : 'W',
			'CUU' : 'L',
			'CUC' : 'L',
			'CUA' : 'L',
			'CUG' : 'L',
			'CCU' : 'P',
			'CCC' : 'P',
			'CCA' : 'P',
			'CCG' : 'P',
			'CAU' : 'H',
			'CAC' : 'H',
			'CAA' : 'Q',
			'CAG' : 'Q',
			'CGU' : 'R',
			'CGC' : 'R',
			'CGA' : 'R',
			'CGG' : 'R',
			'AUU' : 'I',
			'AUC' : 'I',
			'AUA' : 'I',
			'AUG' : 'M',
			'ACU' : 'T',
			'ACC' : 'T',
			'ACA' : 'T',
			'ACG' : 'T',
			'AAU' : 'N',
			'AAC' : 'N',
			'AAA' : 'K',
			'AAG' : 'K',
			'AGU' : 'S',
			'AGC' : 'S',
			'AGA' : 'R',
			'AGG' : 'R',
			'GUU' : 'V',
			'GUC' : 'V',
			'GUA' : 'V',
			'GUG' : 'V',
			'GCU' : 'A',
			'GCC' : 'A',
			'GCA' : 'A',
			'GCG' : 'A',
			'GAU' : 'D',
			'GAC' : 'D',
			'GAA' : 'E',
			'GAG' : 'E',
			'GGU' : 'G',
			'GGC' : 'G',
			'GGA' : 'G',
			'GGG' : 'G'
}

def rna_2_protein(rna_seq):
	'''
	Convert RNA to protein sequence
	'''
	codon = ''
	protein = ''
	for i in range(len(rna_seq)):

		if len(codon) == 3:
			if rna_codon[codon] == -1:
				break
			protein += rna_codon[codon]
			codon = rna_seq[i]
		else:
			codon += rna_seq[i]

	return protein

#rna = sys.stdin.read().strip()

#print rna_2_protein(rna)

if __name__ == "__main__":
	with open('./tests/rosalind_prot_1_dataset.txt', 'r') as rna_file:
		rna_seq = rna_file.readline().strip()
		print(rna_2_protein(rna_seq))

