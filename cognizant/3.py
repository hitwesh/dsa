#Second Largest Element in Array: Find the second largest element in an array.
a = list(map(int, input("Enter an array: ").split()))
temp = 0
greatest = 0
for i in a:
    if i>greatest:
        temp = greatest
        greatest = i
print(temp)