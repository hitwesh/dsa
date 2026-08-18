#Write a function to sort an array using the Bubble Sort algorithm
a = list(map(int, input("Enter an array: ").split()))
for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j+1], a[j] = a[j], a[j+1]
print(a)