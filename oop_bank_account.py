class BankAccount:
    def __init__(self, balance, rate):
        self.account_balance = balance
        self.interest_rate = rate
    
    def __str__(self):
        return f"Your bank account balance is: {self.account_balance} with a interest rate of: {self.interest_rate}"

    def deposit(self, amount):
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            print('You do not have enough money in this account')
        else:
            self.account_balance -= amount

    def gain_interest(self):
        self.account_balance += (self.interest_rate/100) * self.account_balance
        
# Testing class and its methods
my_account = BankAccount(0,2)
print(my_account)
my_account.deposit(20)
print(my_account)

# Tested it for all three cases, < == and > the amount in account
my_account.withdraw(10)
print(my_account)

# Testing for interest rates, must be inputted as percentage
my_account.gain_interest()
print(my_account)