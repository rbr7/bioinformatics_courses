f=open('rosalind_hamm.txt')
f=f.readlines()
a=f[0]
b=f[1]
count=0
for i,j in zip(a,b):
    if i != j:
        print(i,j)
        count+=1
print(count)
