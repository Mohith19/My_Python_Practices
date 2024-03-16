
x= [12,42,23,96,7,18,10,133]

#add min and max
min=x[0]
max=x[0]

for i in x:
    if (i>max):
        max = i
    if(i<min):
        min = i
print(max,min)


Max = max + min
Min = max - min


print(Max,Min)