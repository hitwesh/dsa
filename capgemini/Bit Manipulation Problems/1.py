#Find the single number in an array where every other number appears twice
a = list(map(int, input("Enter a list: ").split()))   
result = 0
for num in a:
    result = result^num
print(a[result])