n = list(map(int, input("Enter a list seperated by spaces: ").split()))
p = int(input("Enter the index: "))
p %= len(n)
a = n[p:]+n[:p]
print(a)