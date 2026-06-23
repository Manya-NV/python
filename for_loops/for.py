#numbers 
n=int(input("enter the range of numbers:"))
for i in range (n):
    print(n)

#list printing
my_list=["a","b","c","d","e"]
for x in my_list:
    print(x)

#range 
for j in range(0,100,5):
    print(j)

#strings
name="manya"
for let in name:
    print(let*2)

#enumerate
name="manya"
for index,let in enumerate(name):
    print(let*(index+1))

#index printing
l=[1,2,3,4,5]
for index,num in enumerate(l):
    print(f"{num} is in {index}th index1")

#else with for
for num in l:
    print(num)
else:
   print(" printed")

#dictinaries
d={"a":1,"b":2,"c":3}
for key,value in d.items():#covertuing to tuple
    print(key," ",value)

#2 tables
for i in range (1,11):
    print(f"2 X {i} = {2*i}")

#2 to 10 tables
for i in range(2,11):
    for j in range (1,11):
        print(f"{i}X{j}={i*j}")