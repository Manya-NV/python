#Function to find largest of three numbers
def large(a,b,c):
    if a>b and b>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
print(large(a,b,c))