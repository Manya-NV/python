txt=input("enter the string: ")
freq={}
for ch in txt:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)