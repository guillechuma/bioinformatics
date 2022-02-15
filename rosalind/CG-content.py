# This Python file uses the following encoding: utf-8
# this program returns the ID of the string having the highest GC-content, followed by the GC-content of that string.
import sys

class Fasta:
	'''
	Class that represents a FASTA file
	'''

	def __init__(self,f_file):
		self.headers = []
		self.sequences = []
		self.parse(f_file)

	def parse(self, f_file):
		with open(f_file, 'r') as fasta_file:
			sequence = ''
			for line in fasta_file:
				if line[-1] == '\n':
					line = line[:-1]
				if line[0] == '>':
					self.headers.append(line[1:])
					self.sequences.append(sequence)
					sequence = ''
					continue
				else:
					sequence += line

			self.sequences.append(sequence)
		self.sequences.pop(0)

	def get_num_sequences(self):
		return len(self.headers)

	def get_sequence(self, number):
		return (self.headers[number], self.sequences[number])


def cg_content(sequence):
	"""
	Calculates the GC content of a sequence
	"""
	cg = 0
	for nucleotide in sequence:
		if nucleotide == 'C' or nucleotide == 'G':
			cg += 1
	return float(cg) / len(sequence) * 100

def max_cg(fast_file):
	'''
	Calculates the sequence with the highest GC content
	'''
	fast = Fasta(fast_file)

	sequences = fast.get_num_sequences()
	max_fasta = ('','')
	max_cg = -1
	for i in range(sequences):
		fasta = ('','')
		fasta = fast.get_sequence(i)
		cg = cg_content(fasta[1])
		if cg > max_cg:
			max_cg = cg
			max_fasta = fasta

	print(str(max_fasta[0]) + '\n' + str(max_cg))
	return max_fasta[0], max_cg

if __name__ == "__main__":
	max_cg('./tests/rosalind_gc.txt')