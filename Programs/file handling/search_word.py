word=input("enter the word to search: ")
file=open("file.txt","r")
content=file.read()
if word in content:
    print("found")
else:
    print("no")