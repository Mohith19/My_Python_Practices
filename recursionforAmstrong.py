def count(n):
    if(n==0):
        return 0
    return 1+count(n//10)

def AmstrongNum(n,countOfNum):
    if n==0:
        return 0
    return (n%10)**countOfNum+AmstrongNum(n//10,countOfNum)

n=int(input("Enter the Number:"))
countOfNum=count(n)
res=AmstrongNum(n,countOfNum)
if(res==n):
    print("Armstrong Number")
else:
    print("Not an Armstrong NumberS ")
    