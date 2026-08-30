#Given two sorted lists, find their common elements using two pointers.
a = list(map(int, input("Enter the first sorted list (space-separated): ").split()))
b = list(map(int, input("Enter the second sorted list (space-separated): ").split()))
i = 0
j = 0
while i<len(a) and j<len(b):
    if a[i] == b[j]:
        print(a[i])
        i += 1
        j += 1
    elif a[i]<b[j]:
        i += 1
    else:
        j += 1
