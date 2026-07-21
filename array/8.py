a = [1,2,3,4]
b = [5,6,7,8]
c = []
for i in range (max(len(a),len(b))):
    if a[i]>b[i]:
        c.append(a[i])
        c.append(b[i])
    else:
        c.append(b[i])
        c.append(a[i])
print(c)