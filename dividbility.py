'''
Write a prgram in which you take an integer input from user , if that integer
if it is divisible by 3 and 6, print good number
if the integer is divisible by 2 and 7 then print an average number.
if the integer is divisible by 4 or 9 then print awesome number
else print bad.
'''

a = int(input("Enter a number:"))

if a%3==0 and a%6==0:
    print("Good Number")
elif a%2==0 and a%7==0:
    print("Average Number")
elif a%4==0 and a%9==0:
    print("Awesome Number")
else:
    print("Bad Number")
