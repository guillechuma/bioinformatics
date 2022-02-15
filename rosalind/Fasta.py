class Fasta:
	'''
	This class represents a FASTA file
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

	def get_all(self, number):
		return (self.headers[number], self.sequences[number])

	def get_sequence(self, number):
		return self.sequences[number]

	def get_sequences(self):
		return self.sequences

	def get_header(self, number):
		return self.headers[number]