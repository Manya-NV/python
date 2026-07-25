words=["apple","ant","ball","bat","cat"]
res={}
for word in words:
    first=word[0]
    if first not in res:
        res[first]=[]
    res[first].append(word)
print(res)