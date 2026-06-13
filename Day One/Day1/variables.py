"""
Variables are used to store data in a program. They can be of different types, such as integers, floats, strings, and booleans. In Python, you can create a variable by simply assigning a value to it using the equals sign (=). For example:
"""

age=25
name="Ram"
price=100

#now use these variables in a print statement anywhere in the code
print("My name is", name, "and I am", age, "years old. The price of the item is", price)
print ("next year age will be", age+1)

#Reassigning variables
score=0
print("Initial score is", score)
score=score+10
print("score after +10=", score)

#multiple assignment
x,y,z=1,2,3

#Swapping values of variables
x,y=y,x
print("After swapping, x is", x, "and y is", y)

#Assigning the values to the variables'
a=10

#Assigning multiple variables to the same value
b=c=d=20
print("b,c,d=", b,c,d)

"""comma(,) is used then there should be same number of variables and values
e,f,g=30,40,50
whereas eqauls(=) is used when we want to assign the same value to multiple variables
e=f=g=30
"""




