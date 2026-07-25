d={"c":10,"b":8,"a":20}
val=list(d.items())

val.sort(key=lambda x:x[1])
print(val)