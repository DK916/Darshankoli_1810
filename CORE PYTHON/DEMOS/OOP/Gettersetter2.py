class Trader:
    def __init__(self,india,dubai,london):
        self.india=india
        self.dubai=dubai
        self.london=london
        
    def getindia(self):
        return self.india
    
    def setindia(self,newplace):
        self.newplace=newplace
        
    def getdubai(self):
        return self.dubai
    
    def setdubai(self,newd):
        self.newdubai=newd
        
    def getlondon(self):
                return self.london
            
    def setlondon(self,newplace):
                self.newplace=newplace
                
    def display(self):
        print(f"india:{self.india}\t dubai:{self.dubai}\t london:{self.london}")
        
t1=Trader("Gulabjam","Gold","eye")
t2=Trader("TAJ MAHAL","BURJ KHALIPA","i am not sure")
print(t1.getindia())
t1.display()
t2.setlondon("Millennium Wheel")
t2.display()