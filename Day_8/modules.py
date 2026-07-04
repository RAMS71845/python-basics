# """
# Modules- Pull in python started libraries
# """
# import math 
# from random import randint,choice,seed
# import datetime as dt #datetime ko dt bana liya
# print(math.pi)
# print(math.sqrt(144))
# print(math.floor(5.7))
# print(math.ceil(5.3))

# print(randint(1,6))
# print(choice(["ROCK","PAPER","SCISSORS"]))
# print(choice(["ODD","EVEN"]))

# today=dt.date.today()
# print(today)
# print(today.year)
# print(today.month)
# print (today.day)

# # creating a new date
# new_year=dt.date(today.year,12,31)
# my_bday=dt.date(2000,12,12)
# print(my_bday)
# new_year=dt.date("NEW YEAR",new_year)

#JSON
import json
user={"name":"Ram","skills":["py","ai"]}
text=json.dumps(user)
print("user",user)
print("USER JSON",text)
back=json.loads(text)
print(back)