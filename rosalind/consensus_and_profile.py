# This Python file uses the following encoding: utf-8
'''
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

'''
import sys

from Fasta import Fasta

def dna_matrix(fasta_file):
	fast = Fasta(fasta_file)
	sequences = fast.get_sequences()

	return sequences

def profile(dna_matrix):
	# Rows are A, C ,G, T (4xn) matrix
	profile_matrix = [[0 for i in range(len(dna_matrix[0]))],
	[0 for i in range(len(dna_matrix[0]))],
	[0 for i in range(len(dna_matrix[0]))],
	[0 for i in range(len(dna_matrix[0]))]]

	nucl_2_row = { 'A' : 0,
	'C' : 1,
	'G' : 2,
	'T' : 3
	}

	for i in range(len(dna_matrix)):
		for j in range(len(dna_matrix[0])):
			nucleotide = dna_matrix[i][j]
			profile_matrix[nucl_2_row[nucleotide]][j] += 1

	return profile_matrix

def consensus(profile_matrix):

	consensus_dna = ''
	row_2_nuc = ['A','C','G','T']
	dna_len = len(profile_matrix[0])
	for j in range(dna_len):
		max_num = -1
		max_index = -1
		for i in range(len(profile_matrix)):
			if profile_matrix[i][j] > max_num:
				max_num = profile_matrix[i][j]
				max_index = i
		consensus_dna += row_2_nuc[max_index]

	return consensus_dna

def output(profile_matrix, consensus):
	print(consensus)
	print('A: ' + ' '.join(map(str,profile_matrix[0])))
	print('C: ' + ' '.join(map(str,profile_matrix[1])))
	print('G: ' + ' '.join(map(str,profile_matrix[2])))
	print('T: ' + ' '.join(map(str,profile_matrix[3])))


if __name__ == "__main__":
	matrix = dna_matrix('./tests/rosalind_cons.txt')
	prof = profile(matrix)
	consen = consensus(prof)
	output(prof, consen)



