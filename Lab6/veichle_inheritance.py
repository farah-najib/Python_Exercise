'''
1. Veichle Inheritance
Create a Python program that models a hierarchy of vehicles using inheritance. Start with a base class Vehicle, and then create two or more derived classes (e.g., Car, Bicycle, Motorcycle) that inherit from the Vehicle class. Each class should have specific attributes and methods related to the type of vehicle it represents.
1.
Define the Vehicle base class with common attributes such as make, model, and year, and methods like start(), stop(), and fuel_up().
2.
Create derived classes for different types of vehicles, e.g., Car, Bicycle, and Motorcycle. Each derived class should inherit from the Vehicle base class and add attributes and methods specific to that type of vehicle. For example, the Car class might have attributes like num_doors, and the Bicycle class could have attributes like num_gears.
3.
Implement specific methods for each derived class. For instance, the Car class might have a method to honk the horn, and the Bicycle class could have a method to ring the bell.
4.
Create instances of each vehicle type and demonstrate their specific methods and attributes. For example, you can create a car, bicycle, and motorcycle, and call methods like start(), stop(), and their specific methods like honk_horn() or ring_bell().
'''
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print(f"{self.make} {self.model} {self.year} starting...")

    def stop(self):
        print(f"{self.make} {self.model} {self.year} stopping...")

    def fuel_up(self):
        print(f"{self.make} {self.model} {self.year} fueling up...")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def honk_horn(self):
        print("Beep beep!")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def ring_bell(self):
        print("Ring ring!")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_type):
        super().__init__(make, model, year)
        self.engine_type = engine_type

    def rev_engine(self):
        print("Vroom vroom!")


car = Car("Car Factory", "car Model", 2000, 4)
bicycle = Bicycle("Bicycle Factory", "Bicycle Model", 2000, 5)
motorcycle = Motorcycle("Motorcycle Factory", "Motorcycle Model", 2020, " Motorcycle Engine")


car.start()
car.honk_horn()
car.stop()

bicycle.start()
bicycle.ring_bell()
bicycle.stop()

motorcycle.start()
motorcycle.rev_engine()
motorcycle.stop()
