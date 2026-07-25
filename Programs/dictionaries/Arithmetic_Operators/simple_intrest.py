#Calculate simple interest.
P=int(input("enter the principal ammount: "))
R=int(input("enter the annual intrest rate in percentage: "))
T=int(input("enter the time in year: "))
SI= (P*T*R)/100
A=SI+P
print("simple intrest is: ",SI)
print("total amount is: ",A)