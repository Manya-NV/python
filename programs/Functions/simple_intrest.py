#Function to calculate simple interest.
def SI(p,t,r):
    return (p*t*r)/100
p=int(input("p: "))
t=int(input("t: "))
r=int(input("r: "))
print(SI(p,t,r))