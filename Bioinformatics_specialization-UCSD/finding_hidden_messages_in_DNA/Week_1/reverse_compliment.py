
import sys

text = sys.argv[1]

def reverse_comp(sequence):
	rev_com = ''
	for nucleotide in sequence:
		if nucleotide == 'A':
			rev_com = rev_com + 'T'
		elif nucleotide == 'T':
			rev_com = rev_com + 'A'
		elif nucleotide == 'G':
			rev_com = rev_com + 'C'
		elif nucleotide == 'C':
			rev_com = rev_com + 'G'
	rev_com = rev_com[::-1]
	return rev_com
