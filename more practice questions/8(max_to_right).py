n = list(map(int, input("Enter the list seperated by space: ").split()))
greatest = n[len(n)-1]
n[len(n)-1]=-1
for i in range(len(n)-1, -1, -1):
    temp = n[i]
    n[i] = greatest
    if greatest<temp:
        greatest = temp
print(n)