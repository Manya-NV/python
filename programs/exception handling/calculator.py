try:
    a=int(input("a: "))
    b=int(input("b: "))
    print("addition: ",a+b)
    print("multiplication: ",a*b)
    print("division: ",a/b)
except ZeroDivisionError:
    print("cannot be divide by zero")
except ValueError:
    print("invalid")
except Exception as e:
    print(e)