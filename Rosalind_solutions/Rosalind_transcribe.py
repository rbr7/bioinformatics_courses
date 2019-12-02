f=open('rosalind_rna.txt','r')
f=f.readlines()
for i in f:
    print(i.replace('T','U'))
