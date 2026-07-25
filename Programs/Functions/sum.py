#Function to find sum of digits.
def sum(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n//=10
    return sum
n=int(input("enter the number: "))
print(sum(n))
