'''
Wite a program to check the type of triangle, where you take input from the user for 3 sides and classify it accordingly into equilateral,isoscales and scalen triangles
'''

a = int(input("Enter the First side :"))
b = int(input("Enter the Second side :"))
c = int(input("Enter the Third side :"))

if a==b and b==c:
    print("It is an Equilateral Triangle")

elif a==b and b!=c:
    print("It is an isoscales Triangle")

elif a!=b and b!=c:
    print("It is an scalen Triangle")
