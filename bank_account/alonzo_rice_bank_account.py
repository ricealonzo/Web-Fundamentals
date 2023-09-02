



# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)





class BankAccount:
    
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        self.amount = 0 

    
    def deposit(self, amount):
        self.balance += amount 
    
    def withdraw(self, amount):
        self.balance -= amount 
    
    def display_account_info(self):

        print(self.balance)
    
    def yield_interest(self):
        if(self.balance > 0):
            self.balance = self.balance + (self.balance * self.int_rate)






test = BankAccount(.01,300)
test.yield_interest()
test.withdraw(100)
test.deposit(1000)
test.display_account_info()
print(test)