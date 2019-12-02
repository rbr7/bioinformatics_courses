import sys

filename = sys.argv[1]

with open(filename) as file:
	for line in file:
		spectrum = map(int,line.split())

def convolution(spec):
	convolution_list = [str(i-j) for i in spec for j in spec if i-j > 0]
	return convolution_list


