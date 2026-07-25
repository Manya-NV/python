d={"a":10,"b":8,"c":20}
max_key=""
max_val=0
for key in d:
    if d[key]>max_val:
        max_val=d[key]
        max_key=key
print(max_key)