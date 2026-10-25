class Bank:
    def __init__(self,acno,name,balance):
        self.acno=acno
        self.name=name
        self.balance=balance
        
    def getacno(self):
        return self.acno
    
    def setacno(self,accno):
        self.acno=accno
        
    def getname(self):
        return self.name
    
    def setname(self,newname):
        self.name=newname
        
    def getbalance(self):
        return self.balance
    
    def setbalance(self,newbalance):
        self.balance=newbalance
        
    def display(self):
        print(f"accno:{self.acno}\t name:{self.name}\t balance:{self.balance}")
        
b1=Bank(101,"DArshan",9000)
b2=Bank(105,"kartik",800)
print(b1.getacno())

b1.display()

b2.display()

b2.setbalance(2000)

b2.display()