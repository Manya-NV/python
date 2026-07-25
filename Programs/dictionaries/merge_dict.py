d1={"a":1,"b":2}
d2={"c":3,"d":4}
merged={}
for keys in d1:
    merged[keys]=d1[keys]
for keys in d2:
    merged[keys]=d2[keys]
print(merged)