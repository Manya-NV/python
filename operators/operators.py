#assignment operators
x=5 #this is equals to 5
print(x)
x+=5 #this is equals to 10 (x=x+5)
print(x)
x-=5 #this is equals to 5 (x=x-5)
print(x)
x/=5 #this is equals to 1 (x=x/5)
print(x)
x*=5 #this is equals to 5 (x=x*5)
print(x)

#comparison operators
a=10
b=20
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)

#logical operator
p=10
q=11
r=12

print(p<q and q<r and r>p)
print(p<r or q==r or r<=p)
print(p!=q)

#membership operator
my_name="manya"
print("m" in my_name)
print("m" not in my_name)
print("s" in my_name)
print("a" not in my_name)

my_list=[1,2,3,"a","b"]
print("m" in my_list)
print(3 not in my_list) 
print(3 in my_list)
print(3 in my_list and "a" not in my_name)
print(3  not in my_list or "a" not in my_name)

#bitwise operators
m=10 #in binary
n=11 #in binary
print(m&n) #bitwise and
print(m|n) #bitwise or
print(m^n) #bitwise xor
print(~n) #bitwise not
print(m<<1) #left shift
print(n>>2) #right shift
