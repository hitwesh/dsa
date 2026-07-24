def palindrome(s):
    left = 0
    right = len(s)-1
    while left<right:
        if s[left] != s[right]:
            return False
            break
        left += 1
        right -= 1
    return True

a = input("Enter the string: ")
b = palindrome(a)
if b == True:
    print("This is a palindrome")
else:
    print("It is not!")