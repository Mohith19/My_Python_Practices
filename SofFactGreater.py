'''
Take a number input from user ,
check if the sum of factors of that number
is grater than the original number or not.
if yes print yes, else no.

'''

num = int(input("Enter the number: "))
sum=0

for i in range(1, num//2 +1):
    if num%i==0:
        sum = sum+i
        
if sum>num:
    print("Yes")
else:
    print("No")
