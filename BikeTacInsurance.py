'''
Write a program to check the on road price of the bike under the conditions
if the price is greter than 72000/- the income tax is 10% of the ex-showroom price.Insurance will be 15% of the actual price.
if the price is greater than 1.5L and less tthan 2L , the tax would be 25% and insurance will be 20%.
if the price is above 2L then the tax will be 35% and insurance will be 28%.
otherwise then display enter a valid value.
Min price starts at 72000/-
'''

price = int(input("Enter the Price of the vehicle :"))

if price <= 72000:
    print("Enter the valid price")


elif price >= 200000:
    print(" Tax is 35% and insurance is 28%")
    Tax = (35/100)*price
    insurance = (28/100)*price
    print (Tax)
    print (insurance)
elif price >= 150000 and price <= 200000:
    print(" Tax is 25% and insurance is 20%")
    Tax = (25/100)*price
    insurance = (20/100)*price
    print (Tax)
    print (insurance)

elif price >= 72000 and price <= 150000:
    print(" Tax is 10% and insurance is 15%")
    Tax = (10/100)*price
    insurance = (15/100)*price
    print (Tax)
    print (insurance)

onroad = (price+Tax+insurance)
print(onroad)
