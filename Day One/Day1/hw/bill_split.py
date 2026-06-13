print("enter the number of friends:    ")
friends=int(input())
print("enter the bill amount:    ")
bill=float(input())
Tip=bill*0.10
total_bill=bill+Tip
per_person_to_pay=total_bill/friends
print("Each person should pay: ",per_person_to_pay)