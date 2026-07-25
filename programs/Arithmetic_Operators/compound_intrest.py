#Calculate compound interest.
P=int(input("enter the principal ammount: "))
r=float(input("enter the annual intrest rate in decimal: "))
T=int(input("enter the time in year: "))
n=int(input("enter the number of time intrest is componded: "))
A = P * (1 + (r/n)) ** (n*T)
CI=A-P
print("compound intrest is: ",CI)
print("total ammount is: ",A)