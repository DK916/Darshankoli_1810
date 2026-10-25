class Employee:
    def __init__(self,emp_id,name,salary):
        self.empid=emp_id
        self.name=name
        self.salary=salary
        
    def display(self):
        print(f"empid:{self.empid}\t name:{self.name}\t salary:{self.salary}")
        
e1=Employee(23,"Darshan",45000)
e2=Employee(21,"Amit",90000)

e1.display()
e2.display()