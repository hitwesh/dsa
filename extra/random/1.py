#You have write a function that accepts, a string which length is “len”, the string has some “#”, in it you have to move all the hashes to the front of the string and return the whole string back and print it.
a = str(input("Enter a string: ").split())
b = ""
count = 0
for _ in a:
    if _ == '#':
        count+=1
    else:
        b+=_
print(count*"#",b)