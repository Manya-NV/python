class invalidAge(Exception):
    pass
age=int(input("enter age: "))
try:
    if age<18:
        raise invalidAge("not eligible")
    print("eligible")
except invalidAge as e:
    print(e)
