# Create an Employee class using the __str__() method.
# Requirements:
# 1. Create a class named Employee.
# 2. Create an __init__() method that accepts name and salary.
# 3. Store both values using self.
# 4. Create a __str__() method that returns the employee's name and salary.
# 5. Create an object with name "Rahul" and salary 25000.
# 6. Print the object.
# Expected Output:
# Name: Rahul, Salary: 25000


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def __str__(self):
        return f"Name:{self.name}\t Salary={self.salary}"
    
e1=Employee("Rahul",25000)
print(e1)