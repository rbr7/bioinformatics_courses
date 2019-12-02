def reversepalindrome(string):
    rev_string=string[::-1]
    revp=''
    for i in rev_string:
        if i == 'A':
            revp+= 'T'
        elif i == 'T':
            revp+= 'A'
        elif i == 'G':
            revp+= 'C'
        elif i == 'C':
            revp+='G'
    return revp
readf=open('rosalind_revp.txt','r')
next(readf)
readf=readf.readlines()
genome=''
for i in readf:
    i=i.strip("\n")
    genome+=i
print(genome)
listofsites=[]
print(len(genome))
for i in range(4,13):
    print(i)
    for j in range(len(genome) -i + 1):
        if genome[j:j+i] == reversepalindrome(genome[j:j+i]) and 12 >= len(reversepalindrome(genome[j:j+i])) >= 4:
            listofsites.append([j+1,i])
listofsites = sorted(listofsites, key=lambda x: x[0])
output=open('restrictionenzymes.txt','w+')
for i in listofsites:
    output.write('{}\t{}\n'.format(i[0],i[1]))
