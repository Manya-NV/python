num=[1,0,2,0,3,4,0,5]
result=[x for x in num if x!=0]
result+=[0]*num.count(0)
print(result)