#!/usr/bin/env python3

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", help="input file name")
args = parser.parse_args()
with open(args.i,'r') as f:
    file = f.readlines()
num_arr = []
x = []
for l in file:
    x.append(l.split('\t')[0])
    x.append(l.split('\t')[0])
    x.append(l.split('\t')[0])
c = list(set(x))
c.sort()
for chr in c:
    num_arr = []
    for line in file:
        if line.split('\t')[0] == chr:
            num_arr.append(int(line.rstrip().split('\t')[1:][0]))
            num_arr.append(int(line.rstrip().split('\t')[1:][1]))
    num_arr.sort()
    r = list(set(num_arr))
    r.sort()
    res = []
    res2 = []
    j = 0
## this works
    sorted_file = []
    for line in sorted(file, key=lambda line: [int(x) if x.isdigit() else x for x in line.rstrip().split('\t')[0:3]]):
        sorted_file.append(line)
    file_1 = [line for line in sorted_file if f"{chr}\t" in line]
    if chr == 'chrY':
        print(len(file_1))
    for i in range(0, int(len(r))-1, 1):
        val = r[i:i + 2]
        count = 0
        s = 0
        for l in file_1[j:]:
            data = [int(x) if x.isdigit() else x for x in l.rstrip().split('\t')[0:3]]
            if val[1] > data[1] and val[0] < data[2]:
                w = f'{chr}\t' + str(val[0]) + '\t' + str(val[1])
                count += 1
                if s == 0 and val[1] < data[2]:
                    j = file_1.index(l)
                    s = 1
            elif val[0] > data[2]:
                continue
            else:
                break
        if count:
            w = w + '\t' + str(count)
            res2.append(w)
    [print(q) for q in res2][0]