n = list(map(int, input("Enter array separated by space: ").split()))
greatest = n[0]
second = n[0]
for i in range(1, len(n)):
    if n[i] > greatest:
        second = greatest
        greatest = n[i]
    elif n[i] > second:
        second = n[i]
print(second)