n = list(map(int,input("Enter the list seperated by space: ").split()))
b = 0
for i in range(len(n)):
    if n[i]<0:
        b+=1
print("Number of positive numbers are: ",len(n)-b)
print("Number of negative numbers are: ",b)