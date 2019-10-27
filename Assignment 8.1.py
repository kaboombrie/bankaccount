# Brie Prater
# Assignment 8.1
# CIS 245

class Account:  #  This is the main account
    def __init__(self, acct, bal):
        self.account = acct
        self.balance = float(bal)

    def getbal(self):  #  function to display account balance
        print("Your current balance is $" + str(self.balance) + ".")

    def deposit(self):  #  function to add deposit
        userdeposit = input("How much would you like to deposit?")
        self.balance = self.balance + float(userdeposit)
        self.getbal()

    def withdraw(self):  #  function to withdraw funds
        userwd = input("How much would you like to withdraw?")
        self.balance = self.balance - float(userwd)
        self.getbal()

class Checking (Account):  #  Child class account checking
    def __init__(self, acct, bal, minbal, fees):
        Account.__init__(self, acct, bal)
        self.minimum = minbal
        self.charges = fees

    def checkbal(self):  #  function to check checking account balance
        self.minimum = 50.00
        if self.balance > self.minimum:
            print("Your account meets the minimum balance.")
        else:
            self.balance = self.minimum - self.balance
            print("You must deposit $" + str(self.balance) + " to meet the minimum balance of $" + str(self.minimum) + ".")

    def minusfee(self):  #  function to deduct fees
        self.charges = 5.00
        print("Account fee is $" + str(self.charges) + ".")
        self.balance = self.balance - self.charges
        self.getbal()

class Savings (Account):  #  Child class savings account
    def __init__(self, acct, bal, intrate, e, annual):
        Account.__init__(self, acct, bal)
        self.interest = intrate
        self.year = annual
        self.variable = e

    def interest(self):
        self.interest = .02
        self.variable = 2.7182
        finalinvest = float((self.balance * self.variable) ** (self.year * self.interest) + self.balance)
        print("Your investment will total $" + str(round(finalinvest, 2)) + " after " + str(self.year) + " years.")


print("Welcome to Money Holders")
while True:
    try:
        acct = int(input("Please enter your account number:"))
        break
    except ValueError:
        print("Please enter your numerical account number.")
myacct = Checking(acct, 100.00, 50.00, 5.00)
Account.getbal(myacct)
save = input("Press 1 if you would like to invest. Press 2 to return to main menu.")
if save == str(1):
    while True:
        try:
            year = int(input("Please enter how many years you would like to invest your savings:"))
            break
        except ValueError:
            print("Please enter a numerical amount.")
    investment = Savings(acct, 100.00, .02, 2.7182, year)
    Savings.interest(investment)
    save = str(2)
elif save == str(2):
    print("Welcome to main menu:")
    print("Would you like to check a different account balance? \n Press 1 for yes, press 2 for no.")
    while True:
        try:
            acct2 = int(input("Please enter your account number:"))
            break
        except ValueError:
            print("Please enter your numerical account number.")
    myacct2 = Checking(acct2, 25.00, 50.00, 5.00)
    Account.getbal(myacct2)
    Checking.checkbal(myacct2)
else:
    print("Please select 1 for investment or 2 to return to main menu")






