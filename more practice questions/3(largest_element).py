n = list(map(int, input("Enter the elements seperated by space: ").split()))
greatest = 0
for i in range(len(n)):
    if n[i]>greatest:
        greatest = n[i]
print(greatest)