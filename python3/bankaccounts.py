class BankAccount(object):
    """docstring for BankAccount"""
    def __init__(self, amount = 0.0):
        self.balance = float(amount)
        self.history = {}
        self.recordhistory("Account Open", amount = self.balance, balance = self.balance)
    
    def __repr__(self):
        return repr(self.balance)
    
    def showhistory(self):
        timestamps = sorted([i for i in iter(self.history)])
        for i in timestamps:
            print("{0}, {1}".format(i, self.history.get(i)))
    
    def deposit(self, amount = 0.0):
        if amount >= 0:
            self.balance += float(amount)
            self.recordhistory("Deposit", amount, self.balance)
        else:
            raise Exception("Amount, {0}, is negative value.".format(amount))
    
    def withdraw(self, amount = 0.0):
        if self.balance < float(amount):
            raise Exception("You do not have that much cash in your account.\nYou currently have {0}.".format(self.balance))
        elif amount < 0:
            raise Exception("Withdrawal amount must be positive value.")
        self.balance -= float(amount)
        self.recordhistory("Withdrawal", amount, self.balance)
    
    def recordhistory(self, action, amount, balance):
        from datetime import datetime
        now = datetime.now().isoformat(' ')
        self.history[now] = dict(action = action, amount = amount, balance = balance)


a = BankAccount(1234)
a.deposit(1)
a.withdraw(1000)
a.deposit(1000000)
a.withdraw(9.87)
a.showhistory()