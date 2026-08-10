n = str(input("Enter a string: "))
left = 0
right = len(n)-1
while left<right:
    if n[left] != n[right]:
        print("not palindrome")
        break
    left+=1
    right-=1
else:
    print("Palindrome")