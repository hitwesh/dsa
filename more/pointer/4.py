#Determine whether a list is a palindrome using two pointers.
a = list(map(int, input("Enter the list: ").split()))
l = 0
r = len(a)-1
while l<r:
    if a[l]!=a[r]:
        print("Not a palindrome")
        break
    l+=1
    r-=1
else:
    print("Palindrome")