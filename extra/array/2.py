#Reverse an array
a = list(map(int,input("Enter the array elements: ").split()))
for i in range(len(a)-1,-1,-1):
    print(a[i], end=" ")