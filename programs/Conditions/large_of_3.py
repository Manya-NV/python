#Find the largest of three numbers
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if a>b and a>c:
    print(f"{a} is largest")
elif b>a and b>c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")
