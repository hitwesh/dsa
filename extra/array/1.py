#Find the largest and smallest number in an array.
a = list(map(int, input("Enter an array: ").split()))
b = float("-inf")
c = float("inf")
for i in range(len(a)):
    if a[i]>b:
        b = a[i]
    elif a[i]<c:
        c = a[i]
    else:
        continue
print("The largest element is: ",b)
print("The smallest element is: ",c)

