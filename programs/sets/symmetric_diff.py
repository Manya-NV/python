set1={1,2,3,4}
set2={3,4,5,6}
symmetric_set=set()
for i in set1:
    if i not in set2:
        symmetric_set.add(i)
for i in set2:
    if i not in set1:
        symmetric_set.add(i)
print(symmetric_set)        