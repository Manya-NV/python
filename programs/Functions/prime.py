#Function to check prime number
def prime(n):
    if n<=1:
        return False
    for i in range(n):
        if n%10==0:
            return False
    return True
n=int(input("enter the number: "))
print(prime(n))
