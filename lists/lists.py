#lists
my_list=[1,"manya",True,"M"]
print(my_list)
#accesing items 
#indexing
print(my_list[1])
#list inside list
my_list1=[1,"manya",True,[2,3,4]]
print(my_list1)

#list methods

my_list.pop()#removes last item
print(my_list)

my_list.pop(0)#removes first item
print(my_list)

my_list.append("moulya")#adds item to last
print(my_list)

#negative indexing
print(my_list[-1])

#remove
my_list.remove("moulya")
print(my_list)

#insert
my_list.insert(1,"moulya")
print(my_list)

#clear 
my_list.clear() #remove all items in list
print(my_list)

#changing specific element
my_list2=["m","a","n",1]
my_list2[2]="anu"
print(my_list2)

#lists slicing
digits=[1,2,3,4,5,6,7,8,9,10]
print(digits[1:7])#prints from 1 to 6th item
print(digits[:7])#prints from 0 tio 6th item
print(digits[1:])#prints from 1 to last item

#[start:end:step]
print(digits[1::2])

digits1=digits[1::2]
print(digits1)

# length of lists
print(len(digits))

#sort lists
num=[2,1,4,3,10,7]
print(sorted(num))

#sum
print(sum(num))

#common methods 

print(my_list1.index("manya"))

print(num.count(1))

num.reverse()
print(num)

my_list3=[1,2,8,6]
my_list3.sort()
print(my_list3)

#nested lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,9,8]
]
#accessing element in nested lists
print(matrix[0])
print(matrix[1][2]) #item in second row third item