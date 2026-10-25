# Write a Python program to demonstrate Multilevel Inheritance.
# Requirements:
# 1. Create a class Animal with a method eat() that prints "Animal is eating".
# 2. Create a class Dog that inherits from Animal. Add a method bark() that prints "Dog is barking".
# 3. Create a class Puppy that inherits from Dog. Add a method weeps() that prints "Puppy is weeping".
# 4. Create an object of Puppy and call all three methods.

class Animal:
    def eat(self):
        print("Animal is eating")
        
class Dog(Animal):
    def bark(self):
        print("dog is barking")
        
class Puppy(Dog):
    def weeps(self):
        print("Puppy is weeping")
        
p1=Puppy()
p1.eat()
p1.bark()
p1.weeps()