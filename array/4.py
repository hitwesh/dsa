from array import *

val = array('i', [1,2,3,4,5,6,7,8,9])

#copying an array

copyArr = array(val.typecode, (x*2 for x in val))

copyArr.pop(3)

copyArr.remove(5)

for i in range(len(copyArr)):
    print(copyArr[i], end=" ")