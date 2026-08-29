#Find all pairs whose sum equals a given target.
a = list(map(int, input("Enter a list: ").split()))
target = int(input("Enter a target: "))
left = 0
right = len(a)-1
while left<right:
    total = a[left]+a[right]
    if total == target:
        print(a[left],a[right])
    elif total<target:
        left+=1
    else:
        right-=1
