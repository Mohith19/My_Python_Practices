#calculate the differnce of sum of numbers that are div by 6 and not div by 6 in the range of first 30 numbers.


n = int(input("Enter a Number :"))
sof1 = 0
sof2 = 0

for i in range(1,n):
    if i % 6 == 0:
        sof1 = sof1 + i
    else:
        sof2 = sof2 + i

a= sof2 - sof1
print(a)

