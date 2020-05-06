a=0
b=1
n=int(input("Enter the num of Fibonacci Series to be generated:"))
if n<=0:
    print("Not Possible")
elif n==1:
    print(a,end=',')
elif n>=2:
    print(a,end=',')
    print(b,end=',')
    for i in range(2,n):
        c=a+b
        print(c,end=',')
        a=b
        b=c
import math

def isPerfectSquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isFibonacci(m):
    return isPerfectSquare(5*m*m+4) or isPerfectSquare(5*m*m-4)
num=int(input("\nEnter a number:"))
if isFibonacci(num):
    print("Yes,It is a Fibonacci number.")
else:
    print("No,It is not a Fibonacci number.")



