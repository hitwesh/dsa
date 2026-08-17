#Missing Number in Array: Find the missing number in an array.
a = list(map(int, input("Enter a list: ").split()))
for i in range(a[0], a[-1]+1):
    if i not in a:
        print("The missing number is:", i)
        break