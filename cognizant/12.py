#Write a Python program to check if a given number is prime.
a = int(input("Enter a number: "))
for i in range(2,int(a**0.5)):
    if a%i==0:
        print("not a prime")
        break
else:
    print("prime")