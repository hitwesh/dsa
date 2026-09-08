#creating a simple class in python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("My name is", self.name)
        print("My age iss", self.age)

student1 = Person("Hitesh", "21")
student1.introduce()