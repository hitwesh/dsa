#Elements in the Range: Find elements in a given range in a sorted array.
a = list(map(int, input("Enter the array: ").split()))
start = int(input("Enter the starting element: "))
end = int(input("Enter the starting element: "))
for i in range(start,end+1):
    print (a[i], end = ' ')