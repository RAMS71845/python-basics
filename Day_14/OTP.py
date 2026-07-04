import random

OTP=str(random.randint(100000,999999))
print(OTP)

attempt=3
while attempt>0:
    user_otp=(input("Enter the OTP: "))
    if len(user_otp)!=6 or not user_otp.isdigit():
        print("Enter a valid 6 digit number")
    
    elif user_otp==OTP:
        print("Verified")
        break
   

    else:
        print("Wrong OTP")

    attempt-=1
    print(f"Attempts left:{attempt}")
if attempt==0:
    print("OTP expired!")
    print("-------------")