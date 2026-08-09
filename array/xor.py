N = int(input("Enter the number of elements in the array: "))
a = list(map(int, input("Enter the array entered by space: ").split()))
ans = 0
if N % 2 == 1:
    for i in range(0, N, 2):
        ans^=a[i]
print(ans)
