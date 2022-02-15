# This Python file uses the following encoding: utf-8

# Calculate mass of AA chain 

import sys

# Data structure for the mass of each AA
mass_table = {

	'A': 71.03711,
	'C': 103.00919,
	'D': 115.02694,
	'E': 129.04259,
	'F': 147.06841,
	'G': 57.02146,
	'H': 137.05891,
	'I': 113.08406,
	'K': 128.09496,
	'L': 113.08406,
	'M': 131.04049,
	'N': 114.04293,
	'P': 97.05276,
	'Q': 128.05858,
	'R': 156.10111,
	'S': 87.03203,
	'T': 101.04768,
	'V': 99.06841,
	'W': 186.07931,
	'Y': 163.06333,

}

def count_mass(prot):
	'''
	Return protein mass
	'''
	mass = 0
	for i in prot:
		mass += mass_table[i]

	return mass

if __name__ == "__main__":
	with open('./tests/rosalind_prtm_1_dataset.txt', 'r') as prot_file:
		prot_seq = prot_file.readline().strip()
		print(count_mass(prot_seq))