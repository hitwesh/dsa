#Find the maximum sum of a subarray of size k.
a = list(map(int, input("Enter an array separated by space: ").split()))
k = 3
maximum = float("-inf")
for i in range(0, len(a) - k + 1):
    if a[i] + a[i+1] + a[i+2] > maximum:
        maximum = a[i] + a[i+1] + a[i+2]
        b = a[i]
        c = a[i+1]
        d = a[i+2]
print("(", b, "),(", c, "),(", d, ")")
print("Maximum sum:", maximum)

#sliding window approach (for nerds)

win_sum = sum(a[:k])
m = win_sum
for r in range(len(a)-k+1):
    win_sum += a[r]
    win_sum -= a[r-k]
    m = max(m,win_sum)
print(m)