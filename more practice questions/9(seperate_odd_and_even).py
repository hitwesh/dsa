n = list(map(int, input("Enter the list seperated by space: ").split()))
a = []
b = []
for i in range(len(n)):
    if n[i] == 0:
        continue
    elif n[i] % 2 == 0:
        a.append(n[i])
    else:
        b.append(n[i])
a.extend(b)
print(a)
