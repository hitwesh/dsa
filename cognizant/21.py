#second largest element in an array
n = list(map(int, input("Enter an array: ").split()))
temp = n[0]
greatest = float("-inf")
for i in range(len(n)):
    if n[i]>greatest:
        temp = greatest
        greatest = n[i]
print(temp)