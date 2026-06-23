''' multi
line 
comment'''
G_name=input("Girl_name: ")
B_name=input("Boy_name: ")
G_marks=int(input("Girl_marks: "))#type coversion
B_marks=int(input("Boy_marks: "))
#abs because if boy score more than girl
marks_diff=abs(G_marks-B_marks)
#cocatination of strings
print(G_name+" scores "+str(G_marks)+" and "+B_name+" scores " +str(B_marks)+".Marks difference is "+str(marks_diff))
#formatted strings
print(f"{G_name} scores {G_marks} and {B_name} scores {B_marks} .Marks difference is {str(marks_diff)}")      