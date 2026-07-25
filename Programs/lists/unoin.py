list1=[1,2,3,4]
list2=[3,4,5,6]
union=list1.copy()
for item in list2:
    if item not in list1:
        union.append(item)
print(union)