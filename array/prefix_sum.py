def prefix(a1, l, r):
    a = [0] * len(a1)

    a[0] = a1[0]

    for i in range(1, len(a1)):
        a[i] = a[i - 1] + a1[i]

    if l == 0:
        return a[r]
    else:
        return a[r] - a[l - 1]


arr = list(map(int, input("Enter the array separated by spaces: ").split()))
left = int(input("Enter the left index: "))
right = int(input("Enter the right index: "))

print(prefix(arr, left, right))