class BankAccount():
    def __init__(self, balance):
        self.__balance = balance # private variable
        
    def deposite(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
# account = BankAccount(1000)
# account.deposite(1500)
# print(account.get_balance())
# print(account.__balance)

class BankAccount():
    # credit = 200000
    def __init__(self, balance, credit):
        self.balance = balance # public variable
        self.credit = credit
    
    def deposite(self, amount):
        self.balance += amount
        
    def __get_total_balance(self): # private method
        return self.credit 
    
    def get_balance(self):
        return self.__get_total_balance() + self.balance

    
account = BankAccount(1000, 30000)
print(account.balance) # before
account.deposite(1500)
print(account.balance) # after
print(account.get_balance())
print(account.__get_total_balance())

