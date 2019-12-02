import sys

file_name = sys.argv[1]

def path(reads):
	string = reads[0]
	for read in reads[1:]:
		string = string + read[-1]
	return string


