def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def menu():
    print("1.addition\n2.subtract\n3.multiplication\n4.quit")

while True:
    menu()
    choice=int(input("enter your choice: "))
    if choice==1:
        a=int(input("a: "))
        b=int(input("b: "))
        print("addition: ",add(a,b))
    elif choice==2:
        a=int(input("a: "))
        b=int(input("b: "))
        print("subtraction: ",sub(a,b))
    elif choice==3:
        a=int(input("a: "))
        b=int(input("b: "))
        print("multiplication: ",mul(a,b))
    elif choice==4:
        print("quitting")
        break
    else:
        print("invalid choice")
