#concatination of strings
first_name=input("first_name: ")
last_name=input("last_name: ")
middle_name=input("middle_name: ")
ful_name = first_name+middle_name+last_name
print(ful_name)

#repetation
message=" warning!.. "
print(message*100)

#string methods
print(message.upper())
print(message.lower())
print(message.strip())
print(message.replace("warning!..","error"))

daughter="manya 'vijay' kumar"
print(daughter)
mother='roopa "vijay" kumar'
print(mother)

#multiline strings
sister='''moulya
             vijay
                  kumar'''
print(sister)

#length of string
print(len(daughter))

#indexing
name="manya_vijaykumar"
print(name[1])#index=position-1
print(name[-1])#negative indexing

#splicing
print(name[3:9])
print(name[:9])# prints from 0 to 9
print(name[3:])# prints from 3 to last index
print(name[-3:-9])#negative splicing

#start end step
print(name[::2])
print(name[1:15:2])