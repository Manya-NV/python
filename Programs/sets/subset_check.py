set1={1,2,3}
set2={1,2}
count=0
for i in set1:
    if i in set2:
        count+=1
if count==len(set1):
    print("subset")
else:
    print("not")