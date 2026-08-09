a = str(input("Enter a string: ").split())
a = a.upper()
b = ['A','E','I','O','U']
q=0
for i in range(len(a)):
    if a[i] in b:
        q+=1
print(q)
    