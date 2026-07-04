"""
Default values
"""
def greet(name,greeting ="HI"):
    print(f"{greeting},{name}")

greet("Ram")#HI,Ram
greet("Ram","Welcome")#Welcome,Ram
greet("")#HI,

#keyword arguments
def book_tickets(name,seat,price):
    print(f"{name} -->seat{seat} (Rs {price})")

book_tickets("Ram","3b",8999)#without keywords it will follow sequence
book_tickets(name="Ram",price=8999,seat="3B")#with keywords mixning can happen
book_tickets("Ravi ku yadav",price=6455,seat="4f")

def add_cart_item(item,cart=[]):
    cart.append(item)
    return cart
print(" ",add_cart_item("Apple"))
print(" ",add_cart_item("Banana"))
print(" ",add_cart_item("Bread"))

def add_cart(item, cart=None):
    if cart is None:
        cart=[]
    cart.append(item)
    return cart

print(" ", add_cart("Apple"))
print(" ",add_cart("Banana"))
print(" ",add_cart("Bread"))
