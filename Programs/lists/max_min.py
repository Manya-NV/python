num=[1,10,17,16,12,13,20]
max=min=num[0]
for n in num:
    if n > max:       
        max=n
    if n < min:
        min=n
print(f"max is {max} and min is {min}")
