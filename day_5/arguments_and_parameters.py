# """
# parameters- arguments(values you passed)
# """
# def greet(name):
#     """GREET ONE PERSON bY NAME"""
#     print(f"Hello {name}")

# greet("BEN")
# #HERE name is the parameter and the BEN is the parameter which we pass

# #ARGUMENTS can be expression too
# raw="    Ram     "
# greet(raw.strip().lower())

# #Multiple parameter -> matched by positions
# def book_ticket(name,seat,price):
#     """PRINT A BOOKING LINE"""
#     print(f"{name}->Seat : {seat} (Rs {price})")

# book_ticket("Ram","2B","90")

orders=[101,102,103]

def confirm_order(order_id):
    print(f"Order #{order_id} confirmed.Out for Delivery")
for oid in orders:
    confirm_order(oid)
    