s1={1,2,3,4}
s2={2,3,5}
s3={2,3,6}
common=set()
for i in s1:
    if i in s2 and i in s3:
        common.add(i)
print(common)
