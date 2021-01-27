#!/usr/bin/python
#standard imports
import sys

with open(sys.argv[3]) as f:
    gene_file = dict.fromkeys([x.replace('\n','') for x in f.readlines()[1:]])
with open(sys.argv[2]) as f:
    ref_file = f.readlines()
for k in gene_file.keys():
    if not gene_file[k]:
        gene_file[k] = [x.split('\t')[0] for x in ref_file if k == x.split('\t')[4]][0]
with open(sys.argv[1]) as f:
    known_file = [x.split('\t')[:5] for x in f.readlines()]
[print("Gene",'\t',"Chr",'\t',"Start",'\t',"Stop")][0]
for k,v in gene_file.items():
    [print(k,'\t',x[1],'\t',x[3],'\t',x[4]) for x in known_file if v in x][0]