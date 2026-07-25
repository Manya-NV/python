#Check whether a number is divisible by 5 and 11
number=int(input("enter the number: "))
if number%5==0:
    print("number is divisible by 5 ")
elif number%11==0:
    print("number is divisible by 11 ")
else:
    print("number is not divisible by 5 and 11")