arr = list(map(int, input().split()))
n = len(arr)
left_max = [-1] * n
right_min = [float('inf')] * n
for i in range(1, n):
    left_max[i] = max(left_max[i - 1], arr[i - 1])

for i in range(n - 2, -1, -1):
    right_min[i] = min(right_min[i + 1], arr[i + 1])
for i in range(n):
    if left_max[i] < arr[i] < right_min[i]:
        print(arr[i])
        break
else:
    print(-1)