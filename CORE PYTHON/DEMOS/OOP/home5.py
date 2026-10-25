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


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def getSubject(self):
        return self.subject

    def setSubject(self, new_subject):
        self.subject = new_subject


t1 = Teacher("Ranjit", 35, "Python")

print(t1.getName())
print(t1.getAge())
print(t1.getSubject())

t1.setName("Amit")
t1.setSubject("Data Science")

print("\nAfter Update:")
print(t1.getName())
print(t1.getSubject())
