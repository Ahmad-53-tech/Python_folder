#                           Introduction to Object-Oriented Programming (OOP)
# - OOP: This is a programming paradigm that organizes code using an object and classes instead of functions and logic alone. It is a more
#advanced paradigm.
#
#                                   Procedural Programming
# This is a programming paradigm that follows a step-by-step approach to solving problems. It is based on procedures(also called functions)
#that contain a sequence of instructions to perform a specific task. In Python, procedural programming means writing code in a linear,
#top-down manner using functions to organize and reuse code.
#
#                                  Key Takeaways
# * Procedural programming is simpler and better for small programs.
# * OOP is better for complex applications because it organizes data and behaviour together.
# * OOP provides better code reuse and security through encapsulation and inheritance.
# * Procedural programming uses functions while OOP uses classes and objects.
#
#                                   Reasons for using OOP
# * It helps organize our code better.
# * It encourages reusability.
# * It makes complex code easier to maintain.
# * It models real world entities.
#
#                                   Key OOP Concepts
# Class/Classes: This is a blueprint for creating objects.
# Object: This is an instance of a class.
# Attribute: This are variables that store object data.
# Methods: This are function inside a class that performs actions.
# __init__: This is a constructor method that initialises object attributes.
# self: This refer to the current instance of the class.
#
#                               Types of method in python class.
# Instance Methods(self): An instance is a method that belongs to an instance of a class. It takes self as its first parameter and
#can modify instance attributes.
#                                       Key Point.
# * It uses self to access or modify instance attribute.
# * It can also access class attributes if needed.
# * It is called using an object of the class.
#
# Class Methods(cls): This is a method that belongs to the class instead of an instance. It takes cls as its first parameter and can
#modify class attributes.
#                                       Key Point
# * It uses @classmethod decorator.
# * It works with cls, which refers to the class itself.
# * It can modify class attributes but not instance attributes.
#
# Starting Methods(No self or cls): This is a method inside a class that does not depend on instance(self) or class(cls) attribute.
#It behaves like a normal function inside a class.
#                                       Key Point
# * It uses @staticmethod decorator.
# * No self or cls(cannot modify instance or class attribute).
# * It is used when a function is related to a class but does not depend on any instance or class-specific data.
#
#                       Differences between Class attribute and Instance attribute.
# * A class attribute is shared across all instances of a class. It is defined directly inside the class but outside any method.
#Since it belongs to the class itself, changing its value affects all instances unless an instance specifically overwrites it.
# * On the other hand, an instance attribute is unique to each object of the class. It is created inside the __init__ method using
#self, meaning every instance of the class gets its own separate copy. Modifying an instance attribute only affects that specific
#object and does not impact other instances.
#
#                       Principles of OOP
# - Encapsulation: This is the process of restricting direct access to data and allowing controlled access through
#methods.
#                       How to achieve Encapsulation.
# * Use private variables(prefix with __)
# * Use getter and setter methods to access or modify private attributes.
#
# - Inheritance: This allows a class(child) to inherit properties and methods from another class(parents).
#                           Types of Inheritance
# * Single Inheritance - One Parent, One Child
# * Multiple Inheritance - A child inherits from multiple parents.
# * Multilevel Inheritance - A child inherits from another child class.
#
# - Polymorphism: This allows the same method name to work differently in different classes. They are two types:
# * Method Overriding (Runtime polymorphism): A child class modifies the behaviour of a parent class method.
# * Method Overloading (Compiled-time Polymorphism): A class has multiple methods with the same name but different parameters. Python does not support true method
#overloading like Java or C++. However, we can achieve a similar effect using default arguments or *args.
#
# - Abstraction: This means hiding unnecessary details and only exposing essential features. Abstract classes cannot be instantiated, they only serve as blueprint for
#subclasses.
#                               How to implement Abstraction.
# * Use abstract classes(via abc module).
# * Define abstract methods (methods that subclasses must implement).




from abc import ABC, abstractmethod

class Car:
    def __init__(self, brand, color):
        self.brand = brand # Attribute
        self.color = color # Attribute

    def drive(self):
        print(f"The {self.color} {self.brand} is driving.")


# Creating
my_car = Car("Toyota", "Red")
print(my_car.brand) # Output: Toyota
my_car.drive() # Output: The Red Toyota is driving.


# ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self): # Getter Method
        return self.__balance

    def set_balance(self, amount): # Setter Method
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount # Assigning new Balance


# Creating an object
account = BankAccount(1000)
print(account.get_balance()) #  ✅ Output: 1000

account.set_balance(2000) # ✅ Setting new balance
print(account.get_balance()) # Output: 2000

# account.set_balance(-500) # ❌ Raises ValueError
# print(account.__balance) # ❌ Error: Cannot access private attribute


# INHERITANCE
# SINGLE INHERITANCE
# Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound"

# Child Class (Inherits from Animal) - Dog inherits from Animal, meaning Dog can use Animal attributes and methods.
# The Dog class overrides the speak() method to provide its own implementation.
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# Creating an object of Dog
dog = Dog("Buddy")
print(dog.name) # Output: Buddy
print(dog.speak()) # Output: Woof! Woof!




class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def function(self):
        return "This Appliance has a function"

# Child Class
class WashingMachine(Appliance):
    def __init__(self, brand, capacity):
        super().__init__(brand) # Call the parent class constructor
        self.capacity = capacity

    def function(self):
        return "This washing machine washes clothes."

# Creating an object of WashingMachine
machine = WashingMachine("Whirlpool", "7kg")

print(machine.brand) # Output: Whirlpool (Inherited from Appliance)
print(machine.capacity) # Output: 7kg (Defined in WashingMachine)
print(machine.function()) # Output: This washing machine washes clothes. (Overriden method)


# Multiple Inheritance (One Child, Multiple Parents) - Dog2 inherits from Animal2 and Pet. It has access to methods from both parent classes.
# Parent Class 1
class Animal2:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Parent Class 2
class Pet:
    def play(self):
        return "Playing with Owner."

# Child Class (Inherits from Animal2 and Pet)
class Dog2(Animal2, Pet):
    def speak(self):
        return "Woof! Woof!"

# Creating an object of Dog
dog2 = Dog2("Buddy")
print(dog2.eat()) # Output: Buddy is eating,
print(dog2.play()) # Output: Playing with owner.
print(dog2.speak()) # Output: Woof! Woof!

# Multilevel Inheritance (A Child Inheriting from Another Child)\
class LivingBeing:
    def breathe(self):
        return "Breathing Oxygen"

class Mammal(LivingBeing):
    def warm_blooded(self):
        return "I am Warm-blooded."

class Dolphin(Mammal):
    def swim(self):
        return "I can swim in water"

# Object for Dolphin
flipper = Dolphin()
print(flipper.breathe()) # Output: Breathing oxygen
print(flipper.warm_blooded()) # Output: I am warm-blooded.
print(flipper.swim()) # Output: I can swim in water.


















































