d={"a":10,"b":8,"c":20}
min_key=""
min_val=float('inf')
for key in d:
    if d[key]<min_val:
        min_val=d[key]
        min_key=key
print(min_key)