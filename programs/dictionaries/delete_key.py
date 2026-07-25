d={"c":10,"b":8,"a":20}
key=input("enter the key to delete: ")
if key in d:
    del(d[key])
print(d)