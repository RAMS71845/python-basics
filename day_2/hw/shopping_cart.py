item="Wireless Mouse"
price=799.0
quantity=3
gst_rate=0.18

subtotal=price*quantity
gst=subtotal*gst_rate
total=subtotal+gst

print("Receipt of purchase:-")
print(f"subtotal: Rs {subtotal:.2f}")
print(f"gst: Rs {gst:.2f}")
print(f"total: Rs {total:.2f}")
