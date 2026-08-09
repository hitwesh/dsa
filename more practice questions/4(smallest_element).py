n = list(map(int,input("Enter a list seperated by spaces: ").split()))
smallest = n[1]
for i in range(1,len(n)):
    if n[i]<smallest:
        smallest = n[i]
print(smallest)