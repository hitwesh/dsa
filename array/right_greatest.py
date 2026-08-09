a = list(map(int, input("Enter the array seperated by space: ")))
greatest = a[len(a)-1]
a[a[len]-1] = -1
for i in range(len(a)-2,-1,-1):
    temp = a[i]
    a[i] = greatest
    if greatest<temp:
        greatest = temp
print(a)
    
