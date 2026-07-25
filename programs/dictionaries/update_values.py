d={"c":10,"b":8,"a":20}
key=input()
value=int(input())
if key not in d:
    d[key]=value
print(d)