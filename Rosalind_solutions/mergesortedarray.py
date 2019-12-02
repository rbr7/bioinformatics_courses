def merge(listo,listt):
    i=0
    j=0
    mergedlist=[]
    while i < len(listo) and j < len(listt):
        if listo[i] > listt[j]:
            mergedlist.append(listt[j])
            j+=1
        else:
            mergedlist.append(listo[i])
            i+=1
    while i == len(listo) and j < len(listt):
        mergedlist.append(listt[j])
        j+=1
    while j == len(listt) and i < len(listo):
        mergedlist.append(listo[i])
        i+=1
    return mergedlist
if __name__ == '__main__':
    inputfile = open('rosalind_mer.txt', 'r')
    data = inputfile.readlines()
    n = data[0]
    A = list(map(int, data[1].rstrip().split()))
    m = data[2]
    B = list(map(int, data[3].rstrip().split()))

    result = merge(A, B)
    print(len(A),len(B),len(result))
    outputfile = open('rosalind_out', 'w')
    outputfile.write(' '.join(list(map(str,result))))

    inputfile.close()
    outputfile.close()
