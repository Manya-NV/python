#Print Fibonacci series
n=int(input("enter the rnage of fibonacci: "))
a,b=(0,1)
for i in range (n):
    c=a+b
    a=b
    b=c
print(c,end=" ")
