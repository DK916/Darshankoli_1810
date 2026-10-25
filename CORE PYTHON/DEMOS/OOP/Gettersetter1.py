class Car:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name= name
        self.price=price
        
    def getbrand(self):
        return self.brand
    
    def setbrand(self,newbrand):
        self.newbrand =newbrand
        
    def getname(self):
        return self.name
            
    def setname(self,newname):
        self.newname =newname
        
        
    def getprice(self):
            return self.price
    
    def setprice(self,newprice):
        self.newbrand =newprice
        
    def display(self):
        print(f"Brand:{self.brand}\t name={self.name}\t price={self.price}")
        
c1=Car("BMW","Seden",400000)
c2=Car("MG","Hector",500000)

print(c1.getname())
c1.display()
c2.setprice(800000)
c2.display()