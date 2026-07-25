a=int(input("a: "))
b=int(input("b: "))
try:
    print("ans: ",a/b)
except Exception as e:
    print(f"error: {e}")
else:
    print("no error")
finally:
    print("end...") 