import random
random.seed(10)
seq=''
for _ in range(99):
    seq+=random.choice('ATGC')
nucl_count={}
for i in seq:
    if i not in nucl_count:
        nucl_count[i]=0
    nucl_count[i]+=1
length = len(seq)
for i,j in nucl_count.items():
    nucl_count[i]=j/length
print(nucl_count)
