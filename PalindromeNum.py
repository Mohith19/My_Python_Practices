#Palindrome

n = int(input("Enter the Number:"))

a=n
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10

if a==rev
:
    print("Number is a palindrome")
else:
    print("Not a palindrome")
