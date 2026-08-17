#Counting Elements in Two Arrays: Count the number of elements in two arrays that are equal.
a = list(map(int, input("Enter the array: ").split()))
b = list(map(int, input("Enter the array: ").split()))
count = 0
for i in range(0, len(a)):
    if a[i] in b:
        count+=1
print(count)