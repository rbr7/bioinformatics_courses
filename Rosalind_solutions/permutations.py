def permutation(n):
    lst=[]
    for i in range(1,n+1):
        lst.append(i)
    list_rev=lst[::-1]
    count=1
    for i in list_rev:
        count=count*i
    from itertools import permutations
    l = list(permutations(range(1, n+1)))
    output=open('enumerategeneorders.txt','w+')
    output.write('{}\n'.format(count))
    for i in l:
        output.write(" ".join(str(x) for x in i))
        output.write("\n")
    output.close()



(permutation(7))
