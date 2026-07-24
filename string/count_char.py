def count_char(s):
    a = s.replace(" ","")
    return len(a)
b = input("Enter the string: ")
print(count_char(b))