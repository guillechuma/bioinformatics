# This Python file uses the following encoding: utf-8
import sys

def hamming_distance(seq1, seq2):
	'''
	Calculate hamming distance between two sequences
	'''
	if len(seq1) != len(seq2):
		return -1

	distance = 0
	for i in range(len(seq1)):
		if seq1[i] != seq2[i]:
			distance += 1

	return distance

if __name__ == "__main__":
	with open('./tests/rosalind_hamm.txt', 'r') as dna_file:
		line = dna_file.readline()
		dna_sequence = []

		while line:
			if line[-1] == '\n':
				line = line[:-1]
			
			dna_sequence.append(line)
			line = dna_file.readline()

		print(hamming_distance(dna_sequence[0],dna_sequence[1]))

