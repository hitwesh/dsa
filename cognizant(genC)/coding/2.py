# Vohra went to a movie with his friends in a Wave theatre and during break time he bought pizzas, puffs and cool drinks. Consider the following prices : 
#   Rs.100/pizza
#   Rs.20/puffs
#   Rs.10/colddrink
# Generate a bill for What Vohra has bought.

def pizza(x):
    p=100*x
    return p 

def puffs(y):
    p=20*y
    return p

def colddrink(z):
    p=10*z
    return p

a = int(input("Enter the no of pizzas bought: "))
b = int(input("Enter the no of puffs bought: "))
c = int(input("Enter the no of cold drinks bought: "))

d=pizza(a)
e=puffs(b)
f=colddrink(c)

print("Bill detail")
print("No of pizzas: ",a)
print("No of puffs: ",b)
print("No of colddrink: ",c)
print("Total price = ",d+e+f)


