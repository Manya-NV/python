#Find the sum of first N natural numbers
N=int(input("enter the first N natural numbers: "))
total=0
for i in range (1,N+1):
   total+=i
print(total)