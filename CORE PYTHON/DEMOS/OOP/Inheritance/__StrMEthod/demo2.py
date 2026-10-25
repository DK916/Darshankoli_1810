# Write a Python program using the __str__() method.
# 1. Create a class named Employee.
# 2. Create an __init__() method with name and salary.
# 3. Store both values using self.
# 4. Create a __str__() method that returns the employee's name and salary.
# 5. Create an object with name "Amit" and salary 30000.
# 6. Print the object.

class Employee:
    def __init__(self,name ,salary):
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return f"Name:{self.name}\t Salary:{self.salary}"
e1=Employee("Amit",30000)
print(e1)