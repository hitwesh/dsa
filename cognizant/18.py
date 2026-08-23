target = int(input("Enter the target: "))
array = list(map(int, input("Enter the array: ").split()))
left, total = 0, 0
result = float("inf")
for right in range(len(array)):
    total += array[right]
    while total >= target:
        result = min(right - left + 1, result)
        total -= array[left]
        left += 1
if result == float("inf"):
    print("None found")
else:
    print("The resulted value is:", result)