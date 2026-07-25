sentence=input("enter the sentence: ")
words=sentence.split()
res={}
for word in words:
    if word in res:
        res[word]+=1
    else:
        res[word]=1
print(res)