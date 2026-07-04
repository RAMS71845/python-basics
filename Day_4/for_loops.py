# """
# for loops-run the body once for each item in a collection
# """

# for ch in "AI":
#     print("Letter: ",ch)
#     #Output -> Letter:  A
#               #Letter:  I

# student=["Asha","Rohan","Chetan","Diya"]
# for student in student:
#     print("welcome",student)

#Task : total cart value calculator
cart_prices=[300,499,88,2000]
total=0
for price in cart_prices:
    total +=price
print(f"total: {total}")


#enumerate
leaderboard =["Asha","Ben","chetan"]
for rank,name in enumerate(leaderboard,start=1):
    print(f"# {rank} : {name}")

    #start yaha pr indexing kaha se suru hogi yeh batata hai
    #agr start ka use na krenge toh indexing 0 se start hogi

#task: For a given list of price create a new list
#with 10 % dis
cart_prices=[300,499,88,2000]
discounted_price=[]
for items in cart_prices:
    discount=(0.10*items)
    new_price=items-discount
    discounted_price.append(new_price)
print (discounted_price)