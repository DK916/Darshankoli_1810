#multilevel inheritance
class Electrical:
    def display(self):
        print("Electrical")
        
class machanical:
    def display(self):
        print("machanical")
        
        
        
class macatronix(machanical,Electrical):
    def display(self):
        print("machanical")
m1=Electrical()
        
m1.display()