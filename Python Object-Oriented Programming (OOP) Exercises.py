# https://pynative.com/python-object-oriented-programming-oop-exercise/

# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# v1 = Vehicle(280, 2000)
# print("Velocidad max: ",v1.max_speed, "Kilometraje:" ,v1.mileage)

# OOP Exercise 2: Create a Vehicle class without any variables and methods

# class Vehicle:
#     pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# Given:

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)

#     def __str__(self):
#         return "{} tiene una velocidad maxima de {} y un kilometraje de {}".format(self.name, self.max_speed, self.mileage)

    
# b1 = Bus("colectivo Fiat", 280, 2000)
# print(b1)

# OOP Exercise 4: Class Inheritance

# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

# Use the following code for your parent Vehicle class.

# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage):
#         super().__init__(name, max_speed, mileage)
    
#     def seating_capacity(self, capacity = 50):
#         return super().seating_capacity(capacity=50)

#     def __str__(self):
#         return "{} tiene una velocidad maxima de {} y un kilometraje de {}".format(self.name, self.max_speed, self.mileage)
    
# b1 = Bus("colectivo Fiat", 280, 2000)
# print(b1.seating_capacity())

# OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

# Use the following code for this exercise.
# class Vehicle:
#     color = "Blanco"

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
    
#     def __str__(self):
#         return f"Nombre: {self.name}\nVelocidad maxima: {self.max_speed}\nKilometraje: {self.mileage}\nColor:{Vehicle.color}"

# class Bus(Vehicle):
#     pass
    
# class Car(Vehicle):
#     pass
    
# v1 = Vehicle("Fiat", 280, 50000)
# b1 = Bus("Volvo", 200, 40000)
# c1 = Car("Renault", 180, 60000)
# print(v1)
# print(b1)
# print(c1)

# OOP Exercise 6: Class Inheritance
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any 
# vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on 
# full fare as a maintenance charge. So total fare for bus instance will become the 
# final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class in Bus class.
# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def __init__(self, name, mileage, capacity):
#         super().__init__(name, mileage, capacity)
    
#     def fare(self):
#         return super().fare()*1.10

# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())

# OOP Exercise 7: Check type of an object
# Write a program to determine which class a given Bus object belongs to.
# Given:

# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# tipo = type(School_bus)
# print(tipo)

# OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
# Given:
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity

# class Bus(Vehicle):
#     pass

# School_bus = Bus("School Volvo", 12, 50)
# print(isinstance(School_bus, Vehicle))
