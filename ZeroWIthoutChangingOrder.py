#Print all 0's first then the remaining numbers without disturbing yheir order

x=[2,0,1024,0,40,230,0]


# for i in x:
#     if i ==0:
#         print(i , end =" ")
y=[]
for i in x :
    if i!=0:
        # print(i, end=" ")
        y =y+ [i]

for i in x:
    if i ==0:
        # print(i , end =" ")
        y=y +[i]

print(y)