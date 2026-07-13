from array import *

val = array('i', [1,2,3,4,5,6,7,8,9])

#inserting an element
val.insert(1,50)
val.append(100)
val[2]=200

for i in range(len(val)):
    print(val[i], end=" ")