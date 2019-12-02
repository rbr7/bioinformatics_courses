def mergesort(list):
    if len(list) > 1:
        mid=len(list)//2
        #splits list into two halves
        left=list[:mid]
        right=list[mid:]
        print(left,"l")
        print(right,"r")
        #recursively keeps splitting list into two halves
        mergesort(left)
        mergesort(right)

        a=0
        b=0
        c=0
        #checks for sorting
        print(list,"0")
        print(left,"left")
        print(right,"right")
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c]=left[a]
                a=a+1
                print(list)
            else:
                list[c]=right[b]
                b=b+1
                print(list)
            c=c+1
        #takes care of base cases
        while a < len(left):
            list[c] = left[a]
            a=a+1
            c=c+1
            print(list,"1")

        while b < len(right):
            list[c] = right[b]
            b=b+1
            c=c+1
            print(list,"3")
    return list,print("hi")
a=[3,2,4,5,1,7]
b = mergesort(a)
print(b)
