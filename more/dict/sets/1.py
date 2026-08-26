#Find the first non-repeating element in a list. (using dict)
n = int(input("Enter the number of inputs to be taken: "))
a = {}
for i in range(n):
    value = input("Enter the value: ")
    if value in a:
        a[value]+=1
    else:
        a[value]=1
for value in a:
    if a[value]==1:
        print("First non repeting value", value)
        break

#Find the first non-repeating element in a list. (using sets)
b = set()
c = set()
s = [2,2,3,4,5,5,6,7,8]
for _ in s:
    if _ in b:
        c.add(_)
    else:
        b.add(_)
for _ in s:
    if _ not in c:
        print(_)
        break