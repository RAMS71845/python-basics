"""
Booleans- True/False
"""

is_raining=True
is_sunny=False
print(is_raining)
print(is_sunny)
print("Type==>", type(is_raining))

real_bool= True
# fake_bool="True"

print(type(real_bool))

#Boolean usually comes from questions
age =20
is_adult= age>=18
print("is_adult?",is_adult)

#Task :take user age input and tell is they can vote or not

name=str(input("Enter Your Name-"))
age=int(input("Enter your age"))

can_vote=age>=18
print("You can vote- ",can_vote)

print(True+True+True)#True=1
print(False+2903)#False=0
print(int(True)+int(False))#1
print(int(True),int(False))#1  0

#Typecast to Bool -For Truthiness
print(bool(1))#True
print(bool(0))#False
print(bool("Hi"))#true- becoz its a non empty 
print(bool(""))#False-its empty

