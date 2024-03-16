'''
Check if a given year is leap year or not
if the year is div by 4 and not div by 100
or
if it is div by 400 then it is called a leap year


'''


year = int(input("Enter the Year: "))

if (year % 4 ==0 and year % 100 !=0) or year % 400 ==0:
    print("It is a leap year")
else:
    print("Not a leap year")
