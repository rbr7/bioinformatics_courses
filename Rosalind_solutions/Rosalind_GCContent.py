with open('rosalind_gc.txt') as f:
    f=f.readlines()
    length = len(f)
    i=0
    seqstart=[]
    while i < length:
        if f[i].startswith('>'):
            seqstart.append(i)
        i=i+1
    seqstart.append(length)
    j=0
    while j < len(seqstart)-1:
        print(f[seqstart[j]].split('>')[1])
        s=''
        for i in range(seqstart[j]+1,seqstart[j+1]):
            s+=f[i]
        #print(s)
        G=s.count('G')
        C=s.count('C')
        A=s.count('A')
        T=s.count('T')
        print((G+C)/(A+T+G+C)*100)
        j=j+1
