n = list(map(int, input("Enter the array seperated by space: ").split()))
a = len(n)
b=0
for i in range(a):
    if n[i] % 2 == 0:
        b+=n[i]
print(b)

