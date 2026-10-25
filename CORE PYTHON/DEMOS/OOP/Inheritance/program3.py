class Animal:
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
        
    def display(self):
        return f"Name:{self.name}\t Age:{self.age}"
    
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(breed)
        