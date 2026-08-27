#Find the frequency of every element in a list. (dict)
a = list(map(int, input("Enter the array: ").split()))
b = {}
for x in a:
    if x in b:
        b[x] += 1
    else:
        b[x] = 1
print(b)

#Find the frequency of every element in a list. (sets)
c = set(a)
if x in c:
    print(x, "->", a.count(x))  