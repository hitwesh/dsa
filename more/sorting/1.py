#Implement bubble sort without using sort().
a = list(map(int, input("Enter the list: ").split()))
n = len(a)
Flag = True
while Flag:
    Flag = False
    for i in range(1, n):
        if a[i-1]>a[i]:
            a[i-1], a[i] = a[i], a[i-1]
            Flag = True
print(a)