#Implement Selection Sort
a = list(map(int, input("Enter an unsorted array: ").split()))
n = len(a)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if a[j]<a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]

print(a)