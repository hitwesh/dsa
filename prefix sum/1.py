from array import *

arr = array("i", [43, 6, 64, 23, 86, 28, 56, 95, 40])

prefix = array("i", [0]) * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]

left = int(input("Enter starting index: "))
right = int(input("Enter ending index: "))

if left == 0:
    print(prefix[right])
else:
    print(prefix[right] - prefix[left - 1])