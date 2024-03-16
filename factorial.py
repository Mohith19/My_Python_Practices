'''
Calculate the value of 7 factorial using formulae
'''

a = int(input("Enter a Number :"))
fact=1
for i in range(1,a+1):
    fact = fact * i

print(fact)
