Upi_Payments=[120,750,300,500,90,1200]
total=0
big_payment=0
for amount in Upi_Payments:
    total+=amount
    if amount>=500:
        big_payment+=1
print(f"Total: Rs{total}")
print(f"Big Payments:{big_payment}")    
      
