# This Python file uses the following encoding: utf-8
import sys

from Fasta import Fasta

def graph_maker(fasta_file, k):
        '''
        Create graph and return overlapping ones
        '''
        fast = Fasta(fasta_file)
        sequences = fast.get_sequences()
        graph = []
        for i in range(len(sequences)):
                for j in range(len(sequences)):
                        first_sequence = sequences[i]
                        second_sequence =sequences[j]

                        if (first_sequence[-k:] == second_sequence[:k]) and (i != j):
                                graph.append([fast.get_header(i), fast.get_header(j)])
        return graph

def output(matrix):
        for  i in range(len(matrix)):
                print(matrix[i][0], matrix[i][1])

if __name__ == "__main__":
    test_1 = graph_maker('./tests/rosalind_grph.txt', 3)
    outp = output(test_1)
    print(outp)
