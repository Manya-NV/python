num=[1,2,0,3,4,0,-1,-2,-3,-4,0]
p=0
n=0
z=0
for i in num:
    if i>0:
        p+=1
    elif i<0:
        n+=1
    else:
        z+=1
print(p)
print(z)
print(n)

