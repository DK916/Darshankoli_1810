class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def displayperson(self):
        print("name:",self.name)
        print("age:",self.age)
        
class Student(Person):
    def __init__(self,name,age,roll_no):
        super().__init__(name,age)
        self.roll_no=roll_no
        
    def displayStudent(self):
     print("roll_No:",self.roll_no)
        
s1=Student("darshan",22,49)

s1.displayPerson()
s1.displayStudent()