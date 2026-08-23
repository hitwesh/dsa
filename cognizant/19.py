#Maximum Subarray Sum, Given an integer array, find the contiguous subarray having the largest sum and return that sum.
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
c = a[0]
m = a[0]
for i in range(1, len(a)):
    c = max(a[i], c+a[i])
    m = max(c, m)
print(m)