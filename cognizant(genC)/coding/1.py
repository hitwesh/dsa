#Write a program to calculate the fuel consumption of your truck.The program should ask the user to enter the quantity of diesel to fill up the tank and the distance covered 
# till the tank goes dry.Calculate the fuel consumption and display it in the format (liters per 100 kilometers).

def european_system(f_t,d):
    c = (f_t/d)*100
    print("Liters/100KM")
    print(f"You need a sum of Rs.{c} to cover the trip")
    return 0
def american_system(f_t,d):
    c = ((d*0.6214)/(f_t*0.2642)20)
    print("Miles/gallons")
    print(f"You need a sum of Rs.{c} to cover the trip")
    return 0

a = float(input("Enter the no of liters to fill the tank: "))
b = float(input("Enter the distance covered: "))
european_system(a,b)
american_system(a,b)
