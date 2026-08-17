#Write a Python program to find the factorial of a given number.
a = int(input("Enter a number: "))
for i in range(2, a-1):
    if a%i==0:
        print(i, end=' ')