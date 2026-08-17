#Python Program to Generate Fibonacci Series: Write a Python program to generate the Fibonacci series up to a given number.
n = int(input("Enter the number of sequence to be printed: "))
a = 0
b = 1
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c, end = ' ')