a=int(input("a: "))
b=int(input("b: "))
op=input()
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case default:
        print("invalid")
