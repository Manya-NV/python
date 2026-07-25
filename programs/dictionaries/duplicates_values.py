d={
    "a":10,
    "b":20,
    "c":10,
    "d":20,
    "e":40
}
dup=[]
values=list(d.values())
for val in values:
    count=0
    for v in values:
        if val==v:
            count+=1
    if count>1 and val not in dup:
        dup.append(val)
print(dup)