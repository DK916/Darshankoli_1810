# class Employee:
    
#    class Employee:
    
#     def __init__(self, id, name, sal):
#         self.id = id
#         self.name = name
#         self.sal = sal

#     def getsal(self):
#         return self.sal

#     def setsal(self, newid):
#         self.sal = newid

#     def display(self):
#         print(f"id={self.id}\tName={self.name}\tSal={self.sal}")

# #Emp Ends here.........................


# class Hr(Employee):
#     def __init__(self,id,name,sal,com):
        
#         super(). __init__(id,name,sal,)
        
#         self.com=com
#     def getcom(self):
#         return self.com
        
#     def setcom(self, com):
#         self.com =com
#     def display(self):
#         print(f"Com={self.com}\t")
#         super().display()
        
# class Developer(Employee):
    
#     def getBonus(self):
#         return self.bonus
#     def setBonus(self,ncom):
#       self.bonus=ncom
#     def display(self):
#         print(f"Com={self.bonus}\t")
#         return super().display()
# #class hr ends here......................................................
             
# e1=Employee(1,"Rahul",2222)
# h1=Hr(7,"Darshan",8767,1500)
# d1=Developer(63,"shivraj",8987,563)
# e1.display()
# h1.display()
# d1.display()

# ```python
class Employee:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getsal(self):
        return self.sal

    def setsal(self, newid):
        self.sal = newid

    def display(self):
        print(f"id={self.id}\tName={self.name}\tSal={self.sal}")


# Employee Ends here


class Hr(Employee):

    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        
        self.com = com

    def getcom(self):
        return self.com

    def setcom(self, com):
        self.com = com

    def display(self):
        print(f"Com={self.com}\t")
        super().display()


# HR Ends here


class Developer(Employee):

    def __init__(self, id, name, sal, bonus):
        super().__init__(id, name, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, bonus):
        self.bonus = bonus

    def display(self):
        print(f"Bonus={self.bonus}\t")
        super().display()


# Developer Ends here


e1 = Employee(1, "Rahul", 2222)
h1 = Hr(7, "Darshan", 8767, 1500)
d1 = Developer(63, "Shivraj", 8987, 563)

e1.display()
h1.display()
d1.display()