s1={1,2,3,4,5}
s2={1,2,4}
missing=set()
for i in s1:
    if i not in s2:
        missing.add(i)
print(missing)