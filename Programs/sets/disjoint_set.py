set1={1,2,3}
set2={4,1,5,6}
flag=True
for i in set1:
    if i in set2:
        flag=False
        
if flag:
    print("disjoint")
else:
    print("not")