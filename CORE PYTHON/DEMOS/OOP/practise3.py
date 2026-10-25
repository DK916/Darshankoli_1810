# class Employee:
#     def __init__(self,empid,name,sal):
#         self.empid=empid
#         self.name=name
#         self.sal=sal
# class HR(Employee):    
#     def getname(self):
#         return self.name
    
#     def setname(self,new_name):
#         self.name=new_name
        
#     def getsal(self):
#         return self.sal
    
#     def setsal(self,new_sal):
#         self.sal=new_sal
    
# e1=Employee(22,"Darshan",89000)

# print(e1.getname())
# e1.setname("amit")
# print(e1.getname())

# print(e1.getsal())

# e1.setsal(99000)

# print(e1.getsal()) #can't add value bechase we can't have using parameter
from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self,id1,name1,sal1):
        self.id = id1
        self.name = name1
        self.sal = sal1
        
    def getId(self):
        return self.id
    
    def setId(self,newid):
        self.id = newid

    def getName(self):
        return self.name
    
    def setName(self,newname):
        self.name = newname

    def getSal(self):
        return self.sal
    def setSal(self,newname):
            self.sal = newname
            
    @abstractmethod
    def calSal(self):
        pass
        
        # print(f"The final salary of employee : {self.sal}")

    def __str__(self):
        print(f"Id:{self.id}\t Name:{self.name}\tsalary:{self.sal}")


class Hr(Employee):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com = com
    def getcom(self):
        return self.com
    def setcom(self,newcom):
        self.com = newcom

    def calSal(self):
        print(f"The final salary of Hr : {self.sal + self.com}")

    def display(self):
        print(f"Commision:{self.com}\t")
        return super().display()
        

class Developer(Employee):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus = bonus
    def getbonus(self):
        return self.bonus
    def setcom(self,newbonus):
        self.com = newbonus 

    def calSal(self):
        print(f"The final salary of Developer : {self.sal + self.bonus}")

    def display(self):
        print(f"Bonus:{self.bonus}\t")
        return super().display()
        

# # e1 = Employee(1,"Rahul",40000)
# h1 = Hr(7,"Harman",50000,5000)
# d1 = Developer(63,"Surya",70000,10000)
# # e1.display()
# h1.display()
# d1.display()