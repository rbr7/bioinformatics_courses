#!/usr/bin/python
#standard imports
import sys

k = int(sys.argv[1]) #read first input as k size of kmers
with open(sys.argv[2]) as f: #read input file, remove new line character and concatenate lines
    file = "".join(line.strip() for line in f.readlines()[1:])
kmers, bases = list(), tuple(list('ATGC'))
def generate_kmers(dna_tup: tuple, kmers: list, k: int)-> dict:
    """ method to generate all possible combinations of kmers from dna bases
    :param dna_tup: tuple of dna bases
    :param kmers:   a list containing combinations
    :param k:       k-mer size from user input
    :return:        k-mer combinations dictionary
    """
    while k:
        kmers = [i + list(j) for i in kmers for j in dna_tup]
        return generate_kmers(dna_tup=dna_tup, kmers=kmers, k=k-1)
    return dict.fromkeys([''.join(x) for x in kmers],0)
kmer_dict = generate_kmers(dna_tup=bases, kmers=[kmers], k=k) #create dictionary with kmers as keys
for key in kmer_dict.keys(): #to find number of occurrences of kmers in fasta read file, insert as values to dict
    if key in file: kmer_dict[key] = sum([1 for i in range(0,len(file)-len(key)+1) if file[i:i+len(key)] == key ])
[print(key,'\t',kmer_dict[key]) for key in sorted(kmer_dict.keys()) if kmer_dict[key]][0] #print stdout