class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getAge(self):
        return self.age

    def setAge(self, new_age):
        self.age = new_age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def getRollNo(self):
        return self.roll_no

    def setRollNo(self, new_roll_no):
        self.roll_no = new_roll_no


s1 = Student("Darshan", 22, 49)

print(s1.getName())
print(s1.getAge())
print(s1.getRollNo())

s1.setName("Amit")
s1.setAge(23)
s1.setRollNo(101)

print(s1.getName())
print(s1.getAge())
print(s1.getRollNo())