sentence=input("enter the sentence: ")
words=sentence.split()
res=[]
for word in words:
    if word not in res:
        res.append(word)
print(res)