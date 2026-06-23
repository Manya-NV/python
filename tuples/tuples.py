#tuples
my_tuple=("apple","banana","cherry")
num=(1,2,3,4,5,6,7,8)
print(num)
print(type(num))
print(num[5]) #accessing
print(num[3:7]) #slicing

#conctenation
last_tuple=my_tuple+num
print(last_tuple)

#repetation
digits=(5,6,7)*3
print(digits)

#checking membership
print(1 in num)
print(10 not in num)

#methods
#count
print(num.count(1))

#index
print(my_tuple.index("banana"))

#nested tuples
tup=(1,2,3,(4,5))
print(tup)

#sets
s={1,200,30}
print(s)#sets are unordered and unidexed

s1=set((12,1,3,90)) # another way for creating set
print(s1)
print(s|s1)#union
print(s&s1)#intersection
print(s-s1)#difference

s.add(10)
print(s)
s.remove(1)
print(s)
s.discard(30)
print(s)
s.pop()#remove random 
print(s)
s.clear()
print(s)