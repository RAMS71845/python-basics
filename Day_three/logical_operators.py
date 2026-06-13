"""
Logical operators-and /or/not
combine boolena into one
"""

age=24
salary=45000

#AND
print(age>=18 and salary>=25000 )#True
print(age>=18 and salary>=55000 )#False
#both should be true to get TRUE otherwise False

is_weekend=False
is_holiday=True

#OR
print(is_weekend or is_holiday)
print(False or False)
print(True or True)
#or Will give True is any of them is True otherwise if both are false then it will give False


#NOT
print(not True)
print(not age>=18)

print("----and----")
print(True and True ,True and False ,False and False)
print("----or----")
print(True or True ,True or False ,False or False)


#precedence
#not>and>or

print(True or False and False)
print((True or False)and False)