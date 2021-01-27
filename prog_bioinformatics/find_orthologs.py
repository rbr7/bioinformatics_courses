#!/usr/bin/env python3

import os
import sys
import subprocess
import argparse
import multiprocessing

cpus = multiprocessing.cpu_count()
parser = argparse.ArgumentParser()
parser.add_argument("-i1", help="input file 1")
parser.add_argument("-i2", help="input file 2")
parser.add_argument("-o", help="output file name")
parser.add_argument("-type", help="Sequence type - n/p")

args = parser.parse_args()

path_list = os.environ['PATH'].split(':')
blast_path = [x for x in path_list if 'blast' in x][0]
# make blastdb
db = ['nucl' if args.type == "n" else 'prot'][0]
i1_name = (args.i1).split('.')[0]+'_chr'
i2_name = (args.i2).split('.')[0]+'_chr'
bcmd = f"mkdir db1 db2 seq_data1 seq_data2"
process = subprocess.Popen(bcmd.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
bashCommand_run1 = f"{blast_path}/makeblastdb -in {args.i1} -dbtype {db} -parse_seqids -out ./db1/{i1_name}"
bashCommand_run2 = f"{blast_path}/makeblastdb -in {args.i2} -dbtype {db} -parse_seqids -out ./db2/{i2_name}"
for bashcmd in [bashCommand_run1,bashCommand_run2]:
    process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def blast_func(x,y,z,w):
    with open(f"{x}",'r') as f:
        file = f.readlines()
    file_dict = dict()
    for line in file:
        if line.startswith('>'):
            k = line
            file_dict[k] = []
        elif not line.startswith('>'):
            v = line
            file_dict[k] = file_dict[k]+[v]
        else:
            print(line)
    c = 0
    for k,v in file_dict.items():
        c += 1
        data = [k]+v
        data = ''.join(data)
        with open(f'./{y}/seq_{c}.fasta','w') as f:
            f.write(data)
    blast_type = ['blastn' if args.type == "n" else 'blastp'][0]
    for i in range(0,c):
        bashCommand = f"{blast_path}/{blast_type} -query ./{y}/seq_{i+1}.fasta -task {blast_type} -db ./{z}/{w} -outfmt 7 -out ./{y}/results_seq{i+1}.out -num_threads {cpus}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
    return c

c1 = blast_func(args.i2,"seq_data2","db1",i1_name)
c2 = blast_func(args.i1,"seq_data1","db2",i2_name)
resuls_dict1, resuls_dict2 = dict(),dict()
readme_data = []

#filtering can be done with normalised bit score and query coverage, subject coverage ; but for now implemented basic only

for i in range(0,c1):
    with open(f'./seq_data2/results_seq{i+1}.out','r') as f:
        file = f.readlines()
    for line in file:
        line = line.rstrip()
        if not line.startswith('#'):
            # limit here is normalised bit score
            limit = float(line.split('\t')[-1])/(float(line.split('\t')[7])-float(line.split('\t')[6]))
            #filtering based on e-value threshold
            if float(line.split('\t')[-2]) <= 0.001:
                match = line.split('\t')[:2]
                resuls_dict1[match[0]] = match[0].split('|')[0]+'|'+match[1]
                break
        else:
            readme_data.append(line+'\n')

for i in range(0,c2):
    with open(f'./seq_data1/results_seq{i+1}.out','r') as f:
        file = f.readlines()
    for line in file:
        line = line.rstrip()
        if not line.startswith('#'):
            match = line.split('\t')[:2]
            if (match[0].split('|')[0]+'|'+match[1]) in resuls_dict1.keys():
                #best match filtering , filtering at Evalue threshold
                if match[0] == resuls_dict1[match[0].split('|')[0]+'|'+match[1]] and float(line.split('\t')[-2]) <= 0.001:
                    resuls_dict2[match[0]] = match[0].split('|')[0]+'|'+match[1]
                    break
        else:
            readme_data.append(line + '\n')

data1,data2 = [],[]
for k,v in resuls_dict1.items():
    data1.append(k+'\t')
    data1.append(v+'\n')

for k,v in resuls_dict2.items():
    data2.append(k+'\t')
    data2.append(v+'\n')

with open('results1.txt','w') as f:
    f.write(''.join(data1))
with open('results2.txt','w') as f:
    f.write(''.join(data2))
#find reciprocal best hits
with open('results1.txt','r') as f:
    file1 = f.readlines()
with open('results2.txt','r') as f:
    file2 = f.readlines()
w1,w2 = [],[]
for line in file1:
    l1 = line.rstrip()
    l1 = l1.split('\t')
    l1 = sorted(l1)
    for l in file2:
        l2 = l.rstrip()
        l2 = l2.split('\t')
        l2 = sorted(l2)
        if l1 == l2:
            w1.append(line)
            w2.append(l)

with open(f'{args.o}.output','w') as f:
    f.write(''.join(w1))
total = len(w1)
readme_data.append(f'The total number of orthologous genes found via blast run are : {total}\n\n')
readme_data.append('Listed as follows :- \n\n ')
readme_data.append(''.join(w1))
readme_data.append(f'The total number of orthologous genes found via blast run are : {total}\n\n')
readme_data.insert(0,f'The total number of orthologous genes found via blast run are : {total}\n\n')
with open("README.txt",'w') as f:
    f.write(''.join(readme_data))
retval1 = os.system("rm -r db1 db2 seq_data1 seq_data2")
retval2 = os.system("rm results1.txt results2.txt")