num=[1,10,17,10,13,16,12,13,20]
duplicate=[]
for i in num:
    if num.count(i)>1 and i not in duplicate:
        duplicate.append(i)
print(duplicate)