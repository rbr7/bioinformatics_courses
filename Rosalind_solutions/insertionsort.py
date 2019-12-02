def insertionsort(list):
    for i in range(1,len(list)):
        value=list[i]
        j=i
        while j > 0 and list[j-1] > value:
            list[j]=list[j-1]
            print(list[j])
            j=j-1
        list[j]=value

a=[7,3,2,4]
insertionsort(a)
print(a)
