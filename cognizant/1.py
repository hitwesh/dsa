#Prime Numbers from 1 to N: Given a number N, the task is to find the Prime Numbers from 1 to N.
n = int(input("Enter the number of prime numbers you want to print: "))
a = 0
b = 2
while a<n:
    prime = True
    for i in range(2, int(b**0.5)+1):
        if b % i == 0:
            prime = False
            break
    if prime:
        print(b, end=' ')
        a+=1
    b+=1