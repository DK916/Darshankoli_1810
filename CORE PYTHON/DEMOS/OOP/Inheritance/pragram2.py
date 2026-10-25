
class Person:
    def __init__(self,name):
        self.name=name
        
class Student(Person):
    def __init__(self,name,marks):
        super().__init__(name)
        self.marks=marks
        
s1=Student("Darshan",99)
print(f"Name:{s1.name}\t Marks:{s1.marks}")
