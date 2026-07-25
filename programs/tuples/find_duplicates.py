t=(1,2,5,3,2,4,5,3,2,6,7,5,2)
dup=[]
for i in range(len(t)):
    count=0
    for j in range(len(t)):
        if t[i]==t[j]:
            count+=1
        if count>1 and t[i] not in dup:
            dup.append(t[i]) 
print(dup)