


class BankAccount:

    bank_name = "First National Dojo"
    all_accounts = []

    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: $",self.balance)    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance += self.balance*self.int_rate
        else:
            pass
        return self
    
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    
    # class method to get balance of all accounts

    # @classmethod
    # def all_balances(cls):
    #     sum = 0
    #     # we use cls to refer to the class
    #     for account in cls.all_accounts:
    #         sum += account.balance
    #     return sum
    
    @classmethod
    def list_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()
            print("Interest Rate: $", account.int_rate)
    

account1 = BankAccount(.01, 100)
account2 = BankAccount(.05, 0)

account1.deposit(20).deposit(15).deposit(5).withdraw(9).yield_interest().display_account_info()
account2.deposit(15).deposit(10).withdraw(9).withdraw(1).withdraw(20).withdraw(30).yield_interest().display_account_info()

# BankAccount.all_balances = classmethod(BankAccount.all_balances)
# print(BankAccount.all_balances())

BankAccount.list_info()
# print(BankAccount.all_accounts)
# BankAccount.list_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        # print(self.account.balance)

    def display_user_balance(self):
        self.account.display_account_info()
        # print(self.account.balance)

user1 = User("John", "john@gmail.com")
user1.make_deposit(100)
user1.make_withdrawal(50)
user1.display_user_balance()


user2 = User("Jane", "jane@gmail.com")
user2.make_deposit(101)
user2.make_withdrawal(50)
user2.display_user_balance()