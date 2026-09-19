#Implement insertion sort.
a = list(map(int, input("Input an unsorted array: ").split()))
n = len(a)
for i in range(1,n):
    for j in range(i, 0, -1):
        if a[j-1]>a[j]:
            a[j-1], a[j] = a[j], a[j-1]
        else:
            break
print(a)