#!/usr/bin/python
#standard imports
import sys

k = int(sys.argv[1])
with open(sys.argv[2]) as f:
    file = f.readlines()
    if k>0 and k<=len(file[0].split('\t')):
        [print(line.split('\t')[k-1]) for line in file][0]
    else:
        print(f"k value {k} is exceeding the file size")