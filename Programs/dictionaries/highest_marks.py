student={"ram":20,"shyam":30,"ravi":28}
highest=0
for marks in student.values():
    if marks > highest:
        highest=marks
print("highest=",highest)