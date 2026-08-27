#Find the element that appears the most times. (dict)
a = list(map(int, input("Enter an array: ").split()))
b = {}
for x in a:
    if x in b:
        b[x]+=1
    else:
        b[x]=1
ans = max(b, key=b.get)
print(ans)
max = 0
ans = None
for x in b:
    if b[x]>max:
        max = b[x]
        ans = x
print(ans)
