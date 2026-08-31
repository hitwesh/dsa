#Find the first negative number in every window of size k. (for fixed size of k)
a = list(map(int, input("Enter the list seperated by space: ").split()))
k = 3
for i in range(len(a)-k+1):
    if a[i]<0:
        b = a[i]
    elif a[i+1]<0:
        b = a[i+1]
    elif a[i+2]<0:
        b = a[i+2]
    else:
        b = "No negative"
    c = a[i]
    d = a[i+1]
    e = a[i+2]
    print("[",c,"],[",d,"],[",e,"] -> ",b)

#sliding window approach (for nerds and variable size of k)
