num=[1,2,3,2,4,4,5,6,6]
freq={}
for n in num:
    if n  in freq:
        freq[n]+=1
    else:
        freq[n]=1

print(freq)