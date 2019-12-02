f=open('rosalind_dna.txt','r')
f=f.readlines()
for i in f:
    print(i.count('A'))
    print(i.count('C'))
    print(i.count('G'))
    print(i.count('T'))
