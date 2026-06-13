orders=[100,299,499,1299,80]
for amount in orders:
    if amount>1000:
        print(f"we have a BIG order : Rs {amount}-Stop")
        break
    print(f"Checked Rs{amount}: small order")