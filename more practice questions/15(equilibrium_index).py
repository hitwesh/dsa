a = list(map(int, input("Enter the array: ").split()))
total = sum(a)
left = 0
for i in range(len(n)):
    right = total - left - a[i]
    if left == right:
        print(i)
        break
    left += a[i]
else:
    print(-1)