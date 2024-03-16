# take an integer as input from thr user and
#check whether if the number is div by its sum of digits or not

a = int(input("Enter the Number :"))
b=a
sumOfNumbers=0
while(a>0):
    r = a%10
    a = a//10
    sumOfNumbers = sumOfNumbers + r

if b % sumOfNumbers ==0:
    print("Given number is div by sum of numbers")
else:
    print("Given number is Not div by sum of numbers")
