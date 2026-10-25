class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def getAccountNo(self):
        return self.account_no

    def setAccountNo(self, new_account_no):
        self.account_no = new_account_no

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

    def getBalance(self):
        return self.balance

    def setBalance(self, new_balance):
        self.balance = new_balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, name, balance, interest):
        super().__init__(account_no, name, balance)
        self.interest = interest

    def getInterest(self):
        return self.interest

    def setInterest(self, new_interest):
        self.interest = new_interest


s1 = SavingsAccount(1001, "Darshan", 50000, 7.5)

print(s1.getAccountNo())
print(s1.getName())
print(s1.getBalance())
print(s1.getInterest())

s1.setBalance(60000)
s1.setInterest(8.0)

print("\nAfter Update:")
print(s1.getBalance())
print(s1.getInterest())