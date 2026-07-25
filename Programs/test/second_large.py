num=[10,40,20,40,50,30]
l=sl=0
for n in num:
    if n>l:
        sl=l
        l=n
    elif n>sl and n!=l:
        sl=n
print(sl)
