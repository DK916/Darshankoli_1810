class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def getid(self):
        return self.id
    
    def setid(self,newid):
       self.name=newid
       
    def getname(self):
        return self.name
    
    def setname(self,newname):
        self.name=newname
        
    def getsal(self):
        return self.sal
    
    def setsal(self,newsal):
        self.sal=newsal
        
e1=Employee(101,"Darshan",7000)

print(e1.getname())
print(e1.getsal())
e1.setsal(9000)

print(e1.getsal())