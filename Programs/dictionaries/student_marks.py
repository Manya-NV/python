students={}
n=int(input("enter the number of students: "))
for i in range(n):
    name=input("enter the name: ")
    marks=int(input("enter the marks of student: "))
    students[name]=marks
print(students)