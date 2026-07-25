from functools import reduce
num=[1,2,5,4,7,8,4]
res=reduce(lambda a,b:a if a>b else b,num)
print(res)