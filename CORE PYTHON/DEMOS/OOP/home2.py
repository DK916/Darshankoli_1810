class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def getEmpId(self):
        return self.emp_id

    def setEmpId(self, new_id):
        self.emp_id = new_id

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getSalary(self):
        return self.salary

    def setSalary(self, new_salary):
        self.salary = new_salary


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def getDepartment(self):
        return self.department

    def setDepartment(self, new_department):
        self.department = new_department


m1 = Manager(101, "Rahul", 50000, "IT")

print(m1.getEmpId())
print(m1.getName())
print(m1.getSalary())
print(m1.getDepartment())

m1.setSalary(60000)
m1.setDepartment("HR")

print("\nAfter Update:")
print(m1.getSalary())
print(m1.getDepartment())