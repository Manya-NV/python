#Check whether a year is a leap year
year=int(input("enter the year: "))
if (year%4 and year%400)==0 and year%100!=0:
    print(f"{year} id leap year")
else:
    print(f"{year} is not leap year")