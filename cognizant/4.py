#Sum of Elements in an Array: Write a program to find the sum of elements in a given array.
a = list(map(int, input("Enter an array seperated by spaces: ").split()))
sum = 0
for i in a:
    sum+=i
print(sum)
