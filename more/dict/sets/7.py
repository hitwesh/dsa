#Find the union of two lists without duplicates.
a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
inter = set(a) | set(b)
print(inter)