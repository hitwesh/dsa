#Last Duplicate Element in a Sorted Array: Find the last duplicate element in a sorted array.
a = list(map(int, input("Enter the array: ").split()))
n = len(a)
b = []
for i in range(n-1, 0, -1):
    if a[i] == a[i-1]:
        print(a[i])
        break