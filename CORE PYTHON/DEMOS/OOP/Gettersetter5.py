class Mobile:
    def __init__(self,name,brand,ram):
        self.name=name
        self.brand=brand
        self.ram=ram
        
    def getname(self):
        return self.name
    def setname(self,newname):
        self.name=newname
        
    def getbrand(self):
        self.brand
    def setbrand(self,newbrand):
        self.brand=newbrand
        
    def getram(self):
        return self.ram
    def setram(self,newram):
        self.ram=newram
        
    def display(self):
        print(f"Name={self.name}\t brand={self.brand}\t ram={self.ram}")
        
m1=Mobile("Iphone13","Apple",128)
m2=Mobile("S22 ultra","Samsung",512)
print(m1.getname())
m1.display()
m2.display()
m2.setram(256)
m2.display()