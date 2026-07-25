t=(1,2,3,4,5)
l=[]
for items in t:
    l.append(items)
print(l)
new_t=()
for items in l:
    new_t+=(items,)
print(new_t)