try:
    file=open("data.txt","r")
    print(file.reacd())
    file.close()
except FileNotFoundError:
    print("file is not found")