#lists

x = [1,2,3,4,5]
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[0:4:2])
print(x[::-1])

for i in x:
    print(i, end="  ")

x.append(6)
print(x)

x.insert(1,4)
print(x)

