#Write a fun to calculate the sum of first and last digit of a number

def fun(num):
    l = num % 10
    while num>=10:
        num=num//10
    f=num%10
    print(f+l)

fun(1557)