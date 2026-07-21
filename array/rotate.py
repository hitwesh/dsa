a = [4,5,2,7,5,3]
k = 2
k %= len(a)
b = a[k:]+a[:k]
print(b)