#while 
#printing numbers from 1 to n
num=1
while num<=100:
    print(num)
    num=num+1
print("completed")

# printing even numbers from 1 to 100 using break
numbers=1
while True:
    if numbers>100:
        break
    if numbers%2==0:
        print(numbers)
    numbers=numbers+1
print("even numbers printed")

#printing odd numbers using continue statement
a=1
while a<=100:
    if a%2 == 0:
        a=a+1
        continue
    print(a)
    a=a+1

# name printing
i=0
while i<=10:
    print("manya",end="-")
    i+=1
  
#nested while
x=1
while x<=10:
    y=5
    while x<=y:
        print("karunya")
        x=x+1

#password
password="manya"
trial=0
while trial<3:
    in_password=input(f"enter the password trail no {trial}")
    trial+=1
    if in_password==password:
        print("logging in")
    else:
        print("incorrect password")


