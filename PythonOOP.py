# Creating classes in Python

class Car:
    # Class Variables
    wheels = 4

    # Constructor of this class

    def __int__(self):
        print("default constructor")

    def __init__(self, color):
        print("Car Class constructor")
        self.color = color

    def test(self):
        print("test method")

    # If any variable is declare inside the method or constructor: They are called instance Variable
    def set_price(self, price):
        self.price = price;

    def getPrice(self):
        return self.price


# How to create an object of the car class

c1 = Car("Red")
print(c1.wheels)
print(Car.wheels)

c1.test()
c1.set_price(1000)
print(c1.getPrice())

c2 = Car("Black")
print(c2.wheels)
print(Car.wheels)

c2.test()
c2.set_price(1000)
print(c2.getPrice())

# Creating a blank class
class Pop:
    pass

p1 = Pop()