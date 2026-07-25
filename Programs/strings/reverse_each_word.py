s="hello python"
words=s.split()
res=""
for word in words:
    res+=word[::-1]+" "
print(res.strip())