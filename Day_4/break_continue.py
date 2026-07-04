# """
# Break-> Quit the loop
# continue-skip the round
# """

orders=[100,299,499,1299,80]
for amount in orders:
    if amount>1000:
        print(f"we have a BIG order : Rs {amount}-Stop")
        break
    print(f"Checked Rs{amount}: small order")


# transactions=[300,353,800,2323,343,-213,-213,400]
# income=0
# for amt in transactions:
#     if amt<0:
#         print(f"Skipping refunds{amt}")
#         continue
#     income +=amt
# print(f"Total Income : {income}")


# correct_pin=2006
# counter=3
# while counter>0:
#     user_pin=int(input(f"Enter your pin. {counter}attempt left"))
#     if user_pin==correct_pin:
#         print("sucesss!!")
#         break
#     counter-=1
#     print ("wrong PIN")

# else:
#     print("Card blocked")
