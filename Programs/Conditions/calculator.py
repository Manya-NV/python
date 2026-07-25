#Create a simple calculator using if-elif.
a=int(input("enter the first operator: "))
b=int(input("enter the second operator: "))
op=(input("enter the first operatoin + - * / %: "))
if op=="+":
    print("addition: ",a+b)
elif op=="-":
    print("subtraction: ",a-b)
elif op=="*":
    print("multiplication: ",a*b)
elif op=="/":
    print("division: ",a/b)
elif op=="%":
    print("mudular division: ",a%b)
else:
    print("none")

