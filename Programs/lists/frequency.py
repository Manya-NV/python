num=[1,2,2,3,1,4,1]
freq={}
for i in num:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
    