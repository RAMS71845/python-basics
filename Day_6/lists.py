# """
# List - orderd,changable collections.
# Your everyday container
# """

cart=["Milk","Bread","Maggie","Milk","Bread","Maggie"]
print ("Cart :    ",cart)
# print("First item of the list: ",cart[0])
# print("Last item of the list: ",cart[-1])
# print("Length", len(cart))
# print("Slice: ",cart[0:2])#Stop is not included
# print("'Milk in cart: '","Milk" in cart)


# #Mutation
# cart[0]="coffee"#for replacing
# print(cart)
# cart.append("Rice")#for adding element in last
# cart.insert(0,"Yoyo")#for inserting or adding the element on the desired position through indexes
# print (cart)

# shopping_list=("Jam","Oil","Tealeaves")
# cart.extend(shopping_list)
# print(cart)

# demo=[1,2]
# demo.append([3,4])# append add the whole list inside a list
# print("Demo after append",demo)
# demo=[1,2]
# demo.extend([3,4])#Extend add the elements of one list to another
# print("Demo after append",demo)

# #Removing Items

# remove_item=cart.pop()
# print(cart)
# print(remove_item)
# cart.remove("Maggie")
# print("Cart after removing Maggie",cart)
# print()

# cart.remove("Jam")
# print("Cart after removing jam",cart)
# print()

# # del cart[0]
# print_queue=[]
# print_queue.append("Report.pdf ")
# print_queue.append("Invoice.pdf ")
# print_queue.append("photo.png ")
# print(f"{len(print_queue)}Jobs waiting")
# while print_queue:
#     job=print_queue.pop(0)
#     print(f" printing {job}....({len(print_queue)}jobs remaining)")
# else:
#     print("no actions left")