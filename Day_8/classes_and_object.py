# """
# classes and objects-Blueprint(class)-> instance(Object)
# """
# class Dog:
#     def __init__(self,name,breed):  #SELF->DEFINES the current working object.
#         self.name=name
#         self.breed=breed

# brigado=Dog("Brigado","Labrador")
# cheeku=Dog("Cheeku","Pamelian")

# brigado.name="Dogesh"
# print(cheeku.name,cheeku.breed)

# class Name:
#     def __init__(self,Name,RollNo,Email):
#         self.Name=Name
#         self.RollNo=RollNo
#         self.Email=Email
# sikha=Name("Sikha Tiwari",2133232,"sikha23@gmail.com")
# Ram=Name("Ram Srivastava",230272682,"ramsrivastava007@gmail.com")
# Amit=Name("Amit kumar",6782189,"amiku56@gmai.com")

# print(Ram.Name,Ram.Email,sikha.Email)
# print(Amit)

class BankAccount:
    interest_rate = 4
    
    def __init__(self, owner_name, account_no, balance=0):
        self.owner_name = owner_name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"Deposited: {deposit_amount}. Updated Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, withdrawn):
        if 0 < withdrawn <= self.balance:
            self.balance -= withdrawn
            print(f"Withdrew: {withdrawn}. Updated Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
            
    def show_balance(self):
        print(f"Account No: {self.account_no} | Owner: {self.owner_name} | Balance: {self.balance}")


class SavingsAccount(BankAccount):
    interest_rate = 6
    
    def withdraw(self, withdrawn):
        # Applies both the 30k limit and basic funds availability check
        if withdrawn > 30000:
            print("Cannot withdraw more than 30k at once.")
        elif withdrawn > self.balance:
            print("Insufficient funds.")
        elif withdrawn <= 0:
            print("Please enter a valid amount.")
        else:
            self.balance -= withdrawn
            print(f"Withdrew: {withdrawn}. Updated Balance: {self.balance}")
        

class Current_Account(BankAccount):
    interest_rate = 2
    
    def withdraw(self, withdrawn):
        if 0 < withdrawn <= self.balance:
            self.balance -= withdrawn  # Fixed the original '=' bug to '-='
            print(f"Withdrew: {withdrawn}. Updated Balance: {self.balance}")
        else:
            print("Enter a valid amount to be withdrawn within your available balance.")
        

class Loan_Account(BankAccount):
    def withdraw(self, withdrawn):
        print("Withdrawals are NOT allowed from a Loan Account.")



### How to use it:

# Creating an account (Name, Account Number, Initial Balance)
Ram = SavingsAccount("Ram srivastava", 2500, balance=10000)

# 1. Show Balance
Ram.show_balance()  

# 2. Deposit Money
Ram.deposit(9000)   

# 3. Withdraw Money
Ram.withdraw(4520)  

# Try exceeding the limit
Ram.withdraw(35000)

Bhavya= Loan_Account("Bhavya Srivastava",25001,balance=500000)

Bhavya.withdraw(5000)
Bhavya.deposit(800000)
Bhavya.show_balance()