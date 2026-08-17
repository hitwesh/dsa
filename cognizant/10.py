#Program for Average of an Array: Write a program to find the average of elements in an array.
a=list(map(int, input("Enter the array: ").split()))
b=0
for i in range(0, len(a)):
    b+=a[i]
print(b/len(a))