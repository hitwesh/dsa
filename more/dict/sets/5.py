#Find all duplicate elements in a list. (dict)
a = list(map(int, input("Enter the array: ").split()))
b = {}
for x in a:
    if x in b:
        b[x] += 1
    else:
        b[x] = 1
for x in b:
    if b[x]>1:
        print(x)    