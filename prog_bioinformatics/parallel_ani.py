#!/usr/bin/env python3
# author : B Rohan, Nov 2020
# standard imports

import os
import re
import argparse
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument("-o", help="output file name")
parser.add_argument("-t", help="number of threads to use")
parser.add_argument("file", help="Input file(s)", nargs="+")
args = parser.parse_args()
files = list(args.file)
matrix = [['' if i==e==0 else 100 if i==e else 0 for i in range(len(files)+1)] for e in range(len(files)+1)]
matrix[0] = ['']+files
for i in range(len(files)):
    matrix[i+1][0] = files[i]
global path
path = os.path.abspath(os.getcwd())
def unique_combinations(file_list: list):
    for x,y in enumerate(file_list):
        for z in range(x+1, len(file_list)):
            yield (y, file_list[z])

def call_dnadiff(x):
    # method to call dnadiff
    num1,num2 = int(re.search(r'\d+', x[0]).group()),int(re.search(r'\d+', x[1]).group())
    #alu = ''.join(random.choice(string.ascii_letters) for i in range(5))
    os.system(f"dnadiff -p outputx{num1}{num2} {x[0]} {x[1]} > /dev/null 2>&1")
    fp = open(f'{path}/outputx{num1}{num2}.report')
    for i, line in enumerate(fp):
        if i == 18:
            v = line.split()[1]
    if num1 == 10:
        x1,y1 = 1,num2+1
    elif num2 == 10:
        x1,y1 = num1+1,1
    else:
        x1,y1 = num1+1,num2+1
    fp.close()
    return (v,x1,y1)

pool = multiprocessing.Pool(int(args.t))
res = [pool.map(call_dnadiff, list(unique_combinations(files)))][0]
pool.close()
pool.join()
for r in res:
    matrix[r[1]][r[2]] = matrix[r[2]][r[1]] = r[0]

with open(args.o,'w') as fw:
    for l in matrix:
        fw.write('\t'.join([str(x) for x in l])+'\n')