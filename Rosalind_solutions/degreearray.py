file=open('rosalind_deg.txt','r')
next(file)
file=file.readlines()
network=[]
for i in file:
    i=i.strip("\n").split(" ")
    network.append(i)
dict={}
for i in network:

    if int(i[0]) not in dict:
        dict[int(i[0])]=0
    dict[int(i[0])]+=1
for i in network:
    if int(i[1]) not in dict:
        dict[int(i[1])]=0
    dict[int(i[1])]+=1
dictf={}
for key in sorted(dict.keys()):
    dictf[key] = dict[key]

output=open('degree.txt','w+')
for i,j in dictf.items():
    output.write("{} ".format(j))
