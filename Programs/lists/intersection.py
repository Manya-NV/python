list1=[1,2,3,4]
list2=[3,4,5,6]
intersection=[]
for items in list1:
    if items in list2:
        intersection.append(items)
print(intersection)