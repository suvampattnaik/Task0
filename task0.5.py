a=int(input("Enter lower range:"))
b=int(input("Enter upper range:"))
print("The prime numbers in the interval are:")
for num in range(a,b+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num,end=",")

c=int(input("\nEnter a number:"))
for j in range(2,c-1):
    if(c%j)==0:
        print("No,It is not a prime number.")
        break
else:
    print("Yes,It is a prime number.")
