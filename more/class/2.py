#class about car
class Car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
        self.speed = 0
    def accelerate(self):
        self.speed += 10
    def brake(self):
        self.speed -= 10

car1 = Car("honda", "blue", "civic")
car1.accelerate()
car1.accelerate()
car1.brake()
print(car1.speed)