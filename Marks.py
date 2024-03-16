#Write a program to accept one single marks from users and check if the marks are greater than 35 then print cheated, if the marks equals to 35 print pass, if marks are less than 35 print fail.

a = int(input("Enter Marks :"))

if a<100 and a>0:
    print("Enter appropriate Marks")
elif a > 35:
    print("Cheated")
elif a == 35:
    print("Pass")
elif a < 35:
    print("Fail")

