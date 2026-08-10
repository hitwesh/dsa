a = str(input("Enter a string: "))
b = ""
seen = set()
for char in a:
    if char not in seen:
        b+=char
        seen.add(char)
print(b)