#Find the minimum sum of a subarray of size k.
a = list(map(int, input("Enter an array separated by space: ").split()))
k = 3
minimum = float("inf")
for i in range(0, len(a) - k + 1):
    if a[i] + a[i+1] + a[i+2] < minimum:
        minimum = a[i] + a[i+1] + a[i+2]
        b = a[i]
        c = a[i+1]
        d = a[i+2]
print("(", b, "),(", c, "),(", d, ")")
print("minimum sum:", minimum)

#using sliding window (for nerds)
min_sum = sum(a[:k])
m = min_sum
for r in range(k, len(a)):
    min_sum += a[r]
    min_sum -= a[r-k]
    m = min(m, min_sum)
print(m)
