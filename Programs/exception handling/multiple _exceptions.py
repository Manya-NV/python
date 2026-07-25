try:
    num=int(input("number: "))
    print(10/num)
except ZeroDivisionError:
    print("cannot be divide by zero")
except ValueError:
    print("invalid")
except Exception as e:
    print(e)