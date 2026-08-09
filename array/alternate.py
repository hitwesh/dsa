n1 = int(input("Enter the length of first array: "))
n = list(map(int, input("Enter the array: ").split()))
m1 = int(input("Enter the length of second array: "))
m = list(map(int, input("Enter the array: ").split()))
a = []
for i in range(max(n1, m1)):
    if i < n1:
        a.append(n[i])
    if i < m1:
        a.append(m[i])
print(a)