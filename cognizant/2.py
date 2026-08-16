#Largest Element in Array: Find the largest element in an array.
a = list(map(int, input("Enter an array: ").split()))
greatest = 0
for i in a:
    if i>greatest:
        greatest = i
print(greatest)
