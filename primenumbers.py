n=int(input("Enter a number:"))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n,"is a not prime number")
            break
    else:
        print(n,"is a prime number")
else:
    print("Negative number")
print("That's it  \U0001F605")
