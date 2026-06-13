"""
f-strings:
"""

name="Ram Srivastava"
age =22
location="Lucknow"

#older way
print("You are "+ str(age)+ " Years old")
#new
print(f"You are {age} years old")
print(f"Next year u will be {age+1}")
#f is makes strings to easy to use as it doesnt need any typeConversion 

#Formatting Numbers with f string
price=2499.5
print(f"Print :Rs {price:.2f}") #gives in only 2 decimal places or any n places -for ex -input was -> 2499.5 , output->2499.50
print (f"Price is : {10000000000:,}") # gives seperator for ex -input was -> 10000000000 , output->10,000,000,000
print (f"Price is : Rs{price:,.2f}") #provides both seperator and decimal placed value - for ex -input was -> 2499.5 , output->2,499.50