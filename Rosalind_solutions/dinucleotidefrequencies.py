import random
random.seed(10)
seq=''
for _ in range(100):
    seq+=random.choice('ATGC')
dinucl_count={}
print(seq)
i=0
while i < len(seq)-1:
    if seq[i:i+2] not in dinucl_count:
        dinucl_count[seq[i:i+2]]=0
    dinucl_count[seq[i:i+2]]+=1
    i=i+1
numdinucl=len(seq)-1
for i,j in dinucl_count.items():
    dinucl_count[i]=j/numdinucl
print(dinucl_count)
