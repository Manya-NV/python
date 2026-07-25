s={1,2,3,4,5,6}
element=int(input("enter the element to remove: "))
if element in s:
    s.remove(element)
print(s)