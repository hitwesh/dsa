#Python Program to Find Second Largest Number in Array: Write a Python program to find the second largest number in an array
a = list(map(int, input("Enter an array: ").split()))
b = float('-inf')
c = float('-inf')   
for i in range(len(a)):
    if a[i] > c:
        b = c
        c = a[i]
    elif a[i] > b and a[i] != c:
        b = a[i]
print("Second largest:", b)