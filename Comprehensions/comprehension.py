#list comprehesions
l=[1,2,3,4,5,6]
sum=1
for num in l:
    sum=sum+num
print(sum)

#append 
dl=[]
for num in l:
    dl.append(num*2)
print(dl)

#dict comprehension
d={"A":1,"B":2,"C":3}
for s in d.items():
    print(s)

students=["manya","moulya","dhanya"]
marks=[1,2,3]
stud_mar={}
for index,student in enumerate(students):
    stud_mar[student]=marks[index]
print(stud_mar)
######
m=[x**2 for x in l]
print(m)

s=["manya","moulya","dhanya"]
a={name: len(name) for name in s  }
print(a)

#####
city={"bengaluru":800,
      "hassan":900,
      "mysore":150,
      "manglore":198
      }
big_city={key:value for key,value in city.items() if value>500}
print(big_city)

#list input
y=[int(num) for num in input("enter the list of integers:").split()]
print(y)
