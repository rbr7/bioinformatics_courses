

def reversecompliment(sequence):
    s=""
    for i in sequence:
        if i == "A":
            s+=i.replace("A","T")
        elif i == "T":
            s+=i.replace("T","A")
        elif i == "G":
            s+=i.replace("G","C")
        elif i == "C":
            s+=i.replace("C","G")
    return s[::-1]
f=open('rosalind_revc.txt','r')
f=f.readlines()
for i in f:
    print(reversecompliment(i))
