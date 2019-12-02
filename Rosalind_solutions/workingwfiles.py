file=open('rosalind_ini5.txt','r')
next(file)
file=file.readlines()
output=open('output.txt','w+')
for i in range(len(file)):
    if i % 2 == 0:
        output.write(file[i])
    else:
        pass
