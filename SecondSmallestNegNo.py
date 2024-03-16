# Write a program to find the second smallest negative number from the list, without using sort,max,min

x = [22,-1,42,65,1,-4,6]

min = 0
max = 0
for i in x:
    if min > i :
        max = min
        min = i
    elif max > i and max > min:
        max = i
print(max) 
