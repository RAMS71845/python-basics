"""Build in tools for creating and formating strings"""

text="Ram srivastava"
print(text.upper())# complete strings converts into uppercase
print(text.lower())# complete strings converts into lowercase
print(text.title())#only first letters of each word in the string into upper cas
print(text.capitalize()) # Only the first letter of the entire string into upper case

messy="   hello world        "
print(f"{messy.strip()}")
#messy strip function is used to remove the unnecessary spaces

#method Chaining-
print(messy.strip().upper())
