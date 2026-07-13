from array import *

val = array('i', [1,2,3,4,5,6,7,8,9])

#simple printing using for loop
for i in range(len(val)):
    print(val[i], end=" ")

print('\n')

#dynamic method of printing
for x in val:
    print(x, end= ',')

print('\n')

#printing typecode
print(val.typecode)