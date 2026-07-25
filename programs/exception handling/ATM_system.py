balance=1000
try:
    amt=int(input("enter the withdrwal amt: "))
    if amt>balance:
        raise Exception("insufficient balance ")
    balance-=amt
    print("remaining balance: ",balance)
except ValueError:
    print("enter only numbers")
except Exception as e:
    print(e)