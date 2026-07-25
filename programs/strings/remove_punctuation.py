s="hello world!.."
result=""
for ch in s:
    if ch.isalnum() or ch.isspace():
        result+=ch
print(result)
