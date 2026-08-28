#Given a sorted list, determine whether two numbers sum to a target.
a = [1,3,5,7,9]
target = 10
left = 0
right = len(a)-1
while left<right:
    total = a[left]+a[right]
    if total == target:
        print("Yes")
        break
    elif total<target:
        left+=1
    else:
        right-=1
else:
    print("No")