class Menu:
    def __init__(self):
        self.cart = {}

    def show_menu(self):
        print("\n===== MENU =====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")


class Cart(Menu):
    def __init__(self):
        super().__init__()

    def add_item(self):
        item = input("Enter Item Name: ")

        while True:
            try:
                price = float(input("Enter Price: "))
                if price <= 0:
                    print("Price must be positive.")
                    continue
                break
            except ValueError:
                print("Enter a valid number.")

        while True:
            try:
                quantity = float(input("Enter Quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                break
            except ValueError:
                print("Enter a valid number.")

        if item in self.cart:
            self.cart[item]["quantity"] += quantity
            print("Quantity Updated Successfully.")
        else:
            self.cart[item] = {
                "price": price,
                "quantity": quantity
            }
            print("Item Added Successfully.")

    def remove_item(self):
        item = input("Enter Item Name to Remove: ")

        if item in self.cart:
            del self.cart[item]
            print("Item Removed Successfully.")
        else:
            print("Item Not Found.")

    def view_cart(self):
        if not self.cart:
            print("Cart is Empty.")
            return

        print("\n------ CART ------")

        subtotal = 0

        for item, details in self.cart.items():
            amount = details["price"] * details["quantity"]
            subtotal += amount

            print(f"{item} x {details['quantity']} = ₹{amount:.2f}")

        print("-------------------")
        print(f"Subtotal = ₹{subtotal:.2f}")

    def checkout(self):
        if not self.cart:
            print("Cart is Empty.")
            return

        subtotal = 0

        for details in self.cart.values():
            subtotal += details["price"] * details["quantity"]

        coupon = input("Enter Coupon Code (Leave Blank if None): ").upper()

        discount = 0

        if coupon == "SAVE10":
            discount = subtotal * 0.10

        elif coupon == "FLAT100":
            if subtotal >= 500:
                discount = 100

        total_after_discount = subtotal - discount

        gst = total_after_discount * 0.18

        final_total = total_after_discount + gst

        print("\n======= BILL =======")
        print(f"Subtotal  : ₹{subtotal:.2f}")
        print(f"Discount  : ₹{discount:.2f}")
        print(f"GST (18%) : ₹{gst:.2f}")
        print("----------------------")
        print(f"TOTAL     : ₹{final_total:.2f}")
        print("====================")


cart = Cart()

while True:

    cart.show_menu()

    choice = input("Enter Choice: ")

    if choice == "1":
        cart.add_item()

    elif choice == "2":
        cart.remove_item()

    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.checkout()
        break

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")