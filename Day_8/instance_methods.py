"""
Instance method & attributes
"""

class BankAccount:
    bank_name="HDFC"
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdrwal(self,amount):
        self.balance-=amount
        return self.balance
Ram=BankAccount("Ram Srivastava",10000000)
sikha=BankAccount("Sikha Tiwari")

Ram.deposit(5000)
print(Ram.balance)
print(vars(Ram))

Ram.withdrwal(8000)
print(Ram.balance)

sikha.deposit(90000000000)
print(sikha.balance)
print(vars(sikha))
print(Ram.bank_name)
BankAccount.bank_name="SBI"#yeh line globally sare users k bank name chnge krdegi
sikha.bank_name="Axis"#yeh line perticular user ka bank change krti hogi
print(Ram.bank_name)
print(sikha.bank_name)