# Question: Create a parent class Person and a child class Student.
# Requirements:
# 1. Person class मध्ये name आणि age variables ठेव.
# 2. get_name() आणि get_age() methods बनव.
# 3. set_name() आणि set_age() methods बनव.
# 4. Student class ने Person कडून inheritance घ्यावं.
# 5. Object तयार करून age update कर.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def getname(self):
        return self.name

    def setname(self,newname):
        self.name=newname
        
    def getage(self):
        return self.age
    
    def setage(self,newage):
        self.age=newage
        
class Student(Person):
     pass
 
p1=Student("Darshan",23)
print(p1.getname())
print(p1.getage())
p1.setage(22)
print(p1.getage())