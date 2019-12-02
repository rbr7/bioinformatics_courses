
import sys

file_name = sys.argv[1]

def suffix(t):
	return t[1:]

def prefix(t):
	return t[:-1]



def overlap_graph(reads):
	overlaps = []
	for j in sorted(reads):
		for i in reads:
			if suffix(i) == prefix(j):
				overlaps.append(i + " -> " + j)
	return overlaps

