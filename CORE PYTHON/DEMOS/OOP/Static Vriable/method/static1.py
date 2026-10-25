class Bank:
    Bank_name="HDFC Bank"     #static variable..........................................
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def display(self):
        return f"Name:{self.name} Balance:{self.balance}"
   
b1=Bank("Darshan",9000)
b2=Bank("Amit",7000)

print(b1.display())
print(b1.Bank_name)
print(b2.Bank_name)
print(Bank.Bank_name)