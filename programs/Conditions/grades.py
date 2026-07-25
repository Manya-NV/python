#Calculate grades based on marks
marks=int(input("enter your marks: "))
if marks>89:
    print("distinction")
elif marks>75:
    print("first class")
elif marks>50:
    print("second class")
elif marks>35:
    print(" third class")
else:
    print("failed")