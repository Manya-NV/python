# function
def greet():
    print("hello")

greet()

# parameter
def marriage(boy, girl):   # default argument
    print(f"boy is {boy} and girl is {girl}")
    print(f"{boy} married {girl}")
marriage("mana", "manya")      # positional arguments
marriage("moulya", "kunal")

# default values
def marriage(boy="narendra", girl="moulya"):
    print(f"boy is {boy} and girl is {girl}")
    print(f"{boy} married {girl}")

marriage()

# tables
def tables(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

tables(5)

# returning values
def func(num):
    return int(str(num))

a = 100
b = func(2)
c = a + b
print(c)

# variable length argument
def add(*a):
    print(type(a))
    print(a)

add(1, 2, 3, 4, 5)

# sum of numbers
def addition(*num):
    return sum(num)

print(addition(1, 2, 3, 4))

# key-value pairs
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(manya=100, moulya=50)

# lambda function
add = lambda a, b: a + b
print(add(10, 20))

# sorting list of dictionaries
students = [
    {"name": "chandhan", "marks": 160},
    {"name": "manya", "marks": 120},
    {"name": "roopa", "marks": 130}
]
students.sort(key=lambda x: x["marks"], reverse=True)
print(students)
