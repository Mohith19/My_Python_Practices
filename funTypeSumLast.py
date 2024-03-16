#Write a function which takes two arguements a and b. Typecast the value of second arguement into integer. Then multiply both the arguements and print the last digit of their result.


def num(a,b):
    b= int(b)
    c =a*b
    print(c%10)

num(11,12.3)
