#Find the pair whose sum is closest to a target.
a = list(map(int, input("Enter a list: ").split()))
target = int(input("Enter the target: "))
left = 0
right = len(a) - 1

closest = float("inf")
answer = None

while left < right:

    total = a[left] + a[right]
    difference = abs(total - target)

    if difference < closest:
        closest = difference
        answer = (a[left], a[right])

    if total < target:
        left += 1

    elif total > target:
        right -= 1

    else:
        break

print(answer)
