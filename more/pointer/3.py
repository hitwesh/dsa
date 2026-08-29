#Remove duplicates from a sorted list in-place
a = list(map(int, input("Enter a list: ").split()))
i = 0
for j in range(1,len(a)):
    if a[i]!=a[j]:
        i+=1
        a[i]=a[j]
print(a[:i+1])