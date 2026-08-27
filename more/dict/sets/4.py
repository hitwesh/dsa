#Check whether two lists contain the same elements with the same frequencies. (dict)
a = list(map(int, input("Enter the first list: ").split()))
b = list(map(int, input("Enter the first list: ").split()))
count_a = {}
count_b = {}
for x in a:
    count_a[x] = count_a.get(x, 0) + 1
for x in b:
    count_b[x] = count_b.get(x, 0) + 1

if count_a == count_b:
    print(True)
else:
    print(False)