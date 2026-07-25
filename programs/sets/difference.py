set1={1,2,3,4}
set2={3,4,5,6}
diff=set()
for i in set1:
    if i not in set2:
        diff.add(i)
print(diff)