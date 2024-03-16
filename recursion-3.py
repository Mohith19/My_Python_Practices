"""
write a program to print the given number in reverse order
""" 
def printNumbers(n):
    if(n==0):
        return
    print(n%10)
    printNumbers(n//10)
printNumbers(12345)

