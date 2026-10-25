# Create a Python program using inheritance and method overriding.
# Requirements:
# 1. Create a parent class named Animal.
# 2. Define a method sound() inside Animal that prints "Animal makes a sound".
# 3. Create a child class named Dog that inherits from Animal.
# 4. Override the sound() method inside the Dog class to print "Dog barks".
# 5. Create an object of the Dog class and call the sound() method.


class Animal:
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
d1=Dog()
d1.sound()

