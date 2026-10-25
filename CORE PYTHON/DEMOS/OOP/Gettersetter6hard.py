class BankAccount:
    
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def getAccountNo(self):
        return self.account_no

    def getName(self):
        return self.name

    def getBalance(self):
        return self.balance

    def setAccountNo(self, new_account_no):
        self.account_no = new_account_no

    def setName(self, new_name):
        self.name = new_name

    def setBalance(self, new_balance):
        self.balance = new_balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient Balance")


b1 = BankAccount(101, "Darshan", 50000)

print("Name:", b1.getName())
print("Balance:", b1.getBalance())

b1.deposit(5000)
print("After Deposit:", b1.getBalance())

b1.withdraw(10000)
print("After Withdraw:", b1.getBalance())