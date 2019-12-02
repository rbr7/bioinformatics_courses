file=open('rosalind_maj.txt','r')
#file=open('majorityelesample.txt','r')
file=file.readlines()
file[0]=file[0].strip("\n").split(" ")
total=int(file[0][1])/2
listofnos={}

for i in range(1,len(file)):
    count={}
    file[i]=file[i].strip("\n").split(" ")
    for a in file[i]:
        if a not in count:
            count[a]=0
        count[a]+=1

    for m,n in count.items():
        if n > total:
            listofnos[i]=int(m)
    if i not in listofnos:
        listofnos[i]=-1

output=open('majele.txt','w+')
for i,j in listofnos.items():
    output.write('{} '.format(j))
