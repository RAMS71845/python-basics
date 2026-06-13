"""
while loops
"""

#ANATOMY-> init-> test-> update

# count=1
# while count<=5:
#     print(f"Rep{count} of 5")
#     count+=1
# print("COUNTING COMPLETED \n")


# sec=10
# while sec>=0:
#     print(f"Launching in {sec} seconds")
#     sec-=1
# print("LAUNCHED")

pending_order=["ORD-101","ORD-102","ORD-103"]
while pending_order:
    order=pending_order.pop(0)
    print(f"Processing {order}..shipped")
print("ALL ORDERS PROCESSED!! \n")
#yaha pr "while pending order" -> while True k tarah hai jab tk elemnets rehnge like mai tab tk sari outputs aayngi khali list hotey hi loop skip hogyi

#break keyword

print("Tiny menu-type 'quit' to leave")
while True:
    choice=input("pick (status/help/quit): ").strip().lower()
    if choice=="quit":
        print("Bye")
        break
    elif choice=="status":
        print("All systems UP")
    elif choice=="help":
        print("Commands: Status,help,quit")
    else:
        print(f"Unknown commands : {choice}")
