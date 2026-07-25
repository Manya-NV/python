phonebook={}
n=int(input("enter the number of contacts: "))
for i in range(n):
    name=input("enter the name: ")
    phone=int(input("enter te number: " ))
    phonebook[name]=phone
search=input("enter the name to search: ")
if search in phonebook:
    print(phone)
else:
    print("not found")

