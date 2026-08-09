n = list(map(int, input("Enter the array seperated by spaces: ").split()))
a=[]
b=[]
for i in range(len(n)):
    if n[i]==0:
        a.append(0)
    else:
        b.append(n[i])
b.extend(a)
print(b)