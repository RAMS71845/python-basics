"""
defining functions- a block of code that can be reused
"""

def greet():
    """Print a friendly greeting"""#docstring-ONE LINE DESCRIPTION
    print("Hello,welcome to the JUNGLE!!!")
    
greet()#evoke kr rhe ho,iske bina print nai hoga koi function
greet()#evoke kr rhe ho,iske bina print nai hoga koi function

print(greet)#print function tell its object and at which location in mmemory it is

print(greet.__doc__)#to fetch out the doctstring of the function

# say_bye() agr define krne se pahle evoke krogey toh nai chalega

def say_bye():
    """sign off"""
    print("SEE YOU TOMORROW!!")

say_bye()