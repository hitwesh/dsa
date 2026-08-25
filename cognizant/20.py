#You are given a 2D array. A row is called magical if the sum of all odd numbers in that row is even. Return the number of magical rows.
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))
a = []
for i in range(n):
    rows = list(map(int, input("Enter the row seperated by spaces: ").split()))
    a.append(rows)
count = 0
for i in range(n):
    odd = 0
    for j in range(m):
        if a[i][j]%2!=0:
            odd += a[i][j]
    if odd % 2 == 0:
        count += 1
print("The number of magic rows are: ", count)
