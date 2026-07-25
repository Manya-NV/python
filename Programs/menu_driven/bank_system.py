def menu():
    print("banking system---\n1.Check Balance\n2.Deposit Money\n3.Withdraw Money\n4.Exit")
def check_balance(balance):
    print("balance available is",balance)
def deposit_money(balance):
    amt=int(input("enter the amt to deposit: "))
    balance+=amt
    print("balance available is",balance)
def withdraw_money(balance):
    amt=int(input("enter the withdrwal amt: "))
    if amt<balance:
        balance-=amt
        print(f"{amt} withdrawed sucessfully")
        print("balance available is",balance)
    else:
        print("withdrwal failed due to insufficient balance")
balance=int(input("enter the initial balance: "))
while True:
    menu()
    choice=int(input("enter the choice: "))
    if choice==1:
        check_balance(balance)
    elif choice==2:
        deposit_money(balance)    
    elif choice==3:
        withdraw_money(balance)
    elif choice==4:
        print("exit\nthnak you......")
        break
    else:
        print("invalid choice")
