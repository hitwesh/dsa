#Python Program to Check Palindrome: Write a Python program to check if a given string is a palindrome.
a = str(input("Enter the number: "))
if a==a[::-1]:
    print("palindrome")
else:
    print("not")