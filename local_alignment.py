#Scoring matrix
BLOSUM62 = {
			'A': {'A': 4,'R': -1,'N': -2,'D': -2,'C': 0,'Q': -1,'E': -1,'G': 0,'H': -2,'I': -1,'L': -1,'K': -1,'M': -1,'F': -2,'P': -1,'S': 1,'T': 0,'W': -3,'Y': -2,'V': 0,'B': -2,'Z': -1,'X': 0},
			'R': {'A': -1,'R': 5,'N': 0,'D': -2,'C': -3,'Q': 1,'E': 0,'G': -2,'H': 0,'I': -3,'L': -2,'K': 2,'M': -1,'F': -3,'P': -2,'S': -1,'T': -1,'W': -3,'Y': -2,'V': -3,'B': -1,'Z': 0,'X': -1},
			'N': {'A': -2,'R': 0,'N': 6,'D': 1,'C': -3,'Q': 0,'E': 0,'G': 0,'H': 1,'I': -3,'L': -3,'K': 0,'M': -2,'F': -3,'P': -2,'S': 1,'T': 0,'W': -4,'Y': -2,'V': -3,'B': 3,'Z': 0,'X': -1},
			'D': {'A': -2,'R': -2,'N': 1,'D': 6,'C': -3,'Q': 0,'E': 2,'G': -1,'H': -1,'I': -3,'L': -4,'K': -1,'M': -3,'F': -3,'P': -1,'S': 0,'T': -1,'W': -4,'Y': -3,'V': -3,'B': 4,'Z': 1,'X': -1},
			'C': {'A': 0,'R': -3,'N': -3,'D': -3,'C': 9,'Q': -3,'E': -4,'G': -3,'H': -3,'I': -1,'L': -1,'K': -3,'M': -1,'F': -2,'P': -3,'S': -1,'T': -1,'W': -2,'Y': -2,'V': -1,'B': -3,'Z': -3,'X': -2},
			'Q': {'A': -1,'R': 1,'N': 0,'D': 0,'C': -3,'Q': 5,'E': 2,'G': -2,'H': 0,'I': -3,'L': -2,'K': 1,'M': 0,'F': -3,'P': -1,'S': 0,'T': -1,'W': -2,'Y': -1,'V': -2,'B': 0,'Z': 3,'X': -1},
			'E': {'A': -1,'R': 0,'N': 0,'D': 2,'C': -4,'Q': 2,'E': 5,'G': -2,'H': 0,'I': -3,'L': -3,'K': 1,'M': -2,'F': -3,'P': -1,'S': 0,'T': -1,'W': -3,'Y': -2,'V': -2,'B': 1,'Z': 4,'X': -1},
			'G': {'A': 0,'R': -2,'N': 0,'D': -1,'C': -3,'Q': -2,'E': -2,'G': 6,'H': -2,'I': -4,'L': -4,'K': -2,'M': -3,'F': -3,'P': -2,'S': 0,'T': -2,'W': -2,'Y': -3,'V': -3,'B': -1,'Z': -2,'X': -1},
			'H': {'A': -2,'R': 0,'N': 1,'D': -1,'C': -3,'Q': 0,'E': 0,'G': -2,'H': 8,'I': -3,'L': -3,'K': -1,'M': -2,'F': -1,'P': -2,'S': -1,'T': -2,'W': -2,'Y': 2,'V': -3,'B': 0,'Z': 0,'X': -1},
			'I': {'A': -1,'R': -3,'N': -3,'D': -3,'C': -1,'Q': -3,'E': -3,'G': -4,'H': -3,'I': 4,'L': 2,'K': -3,'M': 1,'F': 0,'P': -3,'S': -2,'T': -1,'W': -3,'Y': -1,'V': 3,'B': -3,'Z': -3,'X': -1},
			'L': {'A': -1,'R': -2,'N': -3,'D': -4,'C': -1,'Q': -2,'E': -3,'G': -4,'H': -3,'I': 2,'L': 4,'K': -2,'M': 2,'F': 0,'P': -3,'S': -2,'T': -1,'W': -2,'Y': -1,'V': 1,'B': -4,'Z': -3,'X': -1},
			'K': {'A': -1,'R': 2,'N': 0,'D': -1,'C': -3,'Q': 1,'E': 1,'G': -2,'H': -1,'I': -3,'L': -2,'K': 5,'M': -1,'F': -3,'P': -1,'S': 0,'T': -1,'W': -3,'Y': -2,'V': -2,'B': 0,'Z': 1,'X': -1},
			'M': {'A': -1,'R': -1,'N': -2,'D': -3,'C': -1,'Q': 0,'E': -2,'G': -3,'H': -2,'I': 1,'L': 2,'K': -1,'M': 5,'F': 0,'P': -2,'S': -1,'T': -1,'W': -1,'Y': -1,'V': 1,'B': -3,'Z': -1,'X': -1},
			'F': {'A': -2,'R': -3,'N': -3,'D': -3,'C': -2,'Q': -3,'E': -3,'G': -3,'H': -1,'I': 0,'L': 0,'K': -3,'M': 0,'F': 6,'P': -4,'S': -2,'T': -2,'W': 1,'Y': 3,'V': -1,'B': -3,'Z': -3,'X': -1},
			'P': {'A': -1,'R': -2,'N': -2,'D': -1,'C': -3,'Q': -1,'E': -1,'G': -2,'H': -2,'I': -3,'L': -3,'K': -1,'M': -2,'F': -4,'P': 7,'S': -1,'T': -1,'W': -4,'Y': -3,'V': -2,'B': -2,'Z': -1,'X': -2},
			'S': {'A': 1,'R': -1,'N': 1,'D': 0,'C': -1,'Q': 0,'E': 0,'G': 0,'H': -1,'I': -2,'L': -2,'K': 0,'M': -1,'F': -2,'P': -1,'S': 4,'T': 1,'W': -3,'Y': -2,'V': -2,'B': 0,'Z': 0,'X': 0},
			'T': {'A': 0,'R': -1,'N': 0,'D': -1,'C': -1,'Q': -1,'E': -1,'G': -2,'H': -2,'I': -1,'L': -1,'K': -1,'M': -1,'F': -2,'P': -1,'S': 1,'T': 5,'W': -2,'Y': -2,'V': 0,'B': -1,'Z': -1,'X': 0},
			'W': {'A': -3,'R': -3,'N': -4,'D': -4,'C': -2,'Q': -2,'E': -3,'G': -2,'H': -2,'I': -3,'L': -2,'K': -3,'M': -1,'F': 1,'P': -4,'S': -3,'T': -2,'W': 11,'Y': 2,'V': -3,'B': -4,'Z': -3,'X': -2},
			'Y': {'A': -2,'R': -2,'N': -2,'D': -3,'C': -2,'Q': -1,'E': -2,'G': -3,'H': 2,'I': -1,'L': -1,'K': -2,'M': -1,'F': 3,'P': -3,'S': -2,'T': -2,'W': 2,'Y': 7,'V': -1,'B': -3,'Z': -2,'X': -1},
			'V': {'A': 0,'R': -3,'N': -3,'D': -3,'C': -1,'Q': -2,'E': -2,'G': -3,'H': -3,'I': 3,'L': 1,'K': -2,'M': 1,'F': -1,'P': -2,'S': -2,'T': 0,'W': -3,'Y': -1,'V': 4,'B': -3,'Z': -2,'X': -1},
			'B': {'A': -2,'R': -1,'N': 3,'D': 4,'C': -3,'Q': 0,'E': 1,'G': -1,'H': 0,'I': -3,'L': -4,'K': 0,'M': -3,'F': -3,'P': -2,'S': 0,'T': -1,'W': -4,'Y': -3,'V': -3,'B': 4,'Z': 1,'X': -1},
			'Z': {'A': -1,'R': 0,'N': 0,'D': 1,'C': -3,'Q': 3,'E': 4,'G': -2,'H': 0,'I': -3,'L': -3,'K': 1,'M': -1,'F': -3,'P': -1,'S': 0,'T': -1,'W': -3,'Y': -2,'V': -2,'B': 1,'Z': 4,'X': -1},
			'X': {'A': 0,'R': -1,'N': -1,'D': -1,'C': -2,'Q': -1,'E': -1,'G': -1,'H': -1,'I': -1,'L': -1,'K': -1,'M': -1,'F': -1,'P': -2,'S': 0,'T': 0,'W': -2,'Y': -1,'V': -1,'B': -1,'Z': -1,'X': -1},
			}

#Sequence matrix seq1:columns and seq2:rows
def create_identity_matrix(seq1,seq2, gap):
	'''
	This functions creates the identity matrix of the 2 sequences
	with the gap rows and columns initialized
	Match or mismatch: diagonal
	Gap in seq1: vertical
	Gap in seq2: diagonal	
	'''
	#Initialize to zero
	identity_matrix = [[0 for i in range(len(seq1)+1)] for j in range(len(seq2)+1)]

	return identity_matrix

def create_traceback_matrix(seq1, seq2):
	'''
	This function creates a traceback matrix
	'''
	#Initialize to zero
	traceback_matrix = [[0 for i in range(len(seq1)+1)] for j in range(len(seq2)+1)]

	return traceback_matrix

def fill_matrix(seq1, seq2, identity_matrix, scoring_matrix, gap):
	'''
	This function fills the identity matrix, based on the scoring matrix
	It also traces the optimal path with in the traceback_matrix
	'''
	#Get the length of both sequences
	len_seq1 = len(identity_matrix[0])
	len_seq2 = len(identity_matrix)

	#Create a matrix to trace back the optimal path
	traceback_matrix = create_traceback_matrix(seq1, seq2)

	#Start filling matrix using dynamic programming
	for i in range(1, len_seq2):	
		for j in range(1, len_seq1):

			#Calculate max score and track the optimal path
			score, traceback_index = max_score(i, j,seq1, seq2, identity_matrix, scoring_matrix, gap)

			#Asign max score to matrix
			identity_matrix[i][j] = score
			
			#Keep track of the movement 
			traceback_matrix[i][j] = traceback_index

	return (identity_matrix, traceback_matrix)

def max_score(i, j,seq1, seq2, identity_matrix, scoring_matrix, gap):
	'''
	This function returns the max score of the three possible alignments 
	in position i and j and returns a key value that identifies the movement
	'''
	#Index 0: match/mismatch
	no_gap = (identity_matrix[i-1][j-1] + scoring_matrix[seq2[i-1]][seq1[j-1]], 0)
	#index 1: seq1 gap
	seq1_gap = (identity_matrix[i-1][j] + gap, 1)
	#index 2: seq2 gap
	seq2_gap = (identity_matrix[i][j-1] + gap, 2)
	#Defining sorting key
	def sort_first(val):
		return val[0]

	scores = [seq1_gap, seq2_gap, no_gap, (0,-1)]
	#Sort the three scores
	scores.sort(key = sort_first)
	#Return the highest score with its identifier

	return scores[-1]

def find_max_value(identity_matrix):
	'''
	This function finds the maximum value of a matrix 
	and returns its value and position
	'''
			   #score, i, j
	max_score = (-1, -1, -1)
	#Get the length of both sequences
	len_seq1 = len(identity_matrix[0])
	len_seq2 = len(identity_matrix)

	for i in range(1, len_seq2):	
		for j in range(1, len_seq1):
			if identity_matrix[i][j] >= max_score[0]:
				max_score = (identity_matrix[i][j], i, j)

	return max_score



def traceback_sequences(seq1,seq2,identity_matrix, traceback_matrix):
	'''
	This function creates the aligned sequences based on the optimal path 
	that led to the optimal sequence in the identity matrix.
	'''
	#The starting indices of the matrix (bottom right)
	max_score, i, j = find_max_value(identity_matrix)

	#The initially empty aligned sequences
	aligned_seq1 = ''
	aligned_seq2 = ''

	#Repeat until the algorithm reaches the position (0,0)
	while (identity_matrix[i][j] != 0):

		#The case when a match/mismatch is optimal
		if traceback_matrix[i][j] == 0:
			aligned_seq1 += seq1[j-1]
			aligned_seq2 += seq2[i-1]
			i -= 1
			j -= 1

		#The case when a gap in sequence 1 is optimal
		elif traceback_matrix[i][j] == 1:
			aligned_seq1 += '-'
			aligned_seq2 += seq2[i-1]
			i -= 1

		#The case when a gap in sequence 2 is optimal
		else:
			aligned_seq1 += seq1[j-1]
			aligned_seq2 += '-'
			j -= 1

	#Return the aligned sequences in reverse order
	return (aligned_seq1[::-1], aligned_seq2[::-1])


def local_alignment(sequence1, sequence2):
	'''
	This function performs a global alignment on sequence1 and sequence2 
	using the Needleman and Wunsch algorithm
	'''
	#User can define gap penalty
	gap = -4

	identity_matrix = create_identity_matrix(sequence1,sequence2, gap)
	complete_matrix, filled_traceback_matrix = fill_matrix(sequence1, sequence2, identity_matrix, BLOSUM62, gap)
	aligned_seq1, aligned_seq2 = traceback_sequences(sequence1, sequence2, complete_matrix, filled_traceback_matrix)

	return (aligned_seq1, aligned_seq2)


def main():
	seq1 = input('Enter sequence 1: ')
	seq2 = input('Enter sequence 2: ')
	a_seq1, a_seq2 = local_alignment(seq1, seq2)
	print('The aligned sequences are:')
	print(a_seq1)
	print(a_seq2)


if __name__ == '__main__':
	main()

