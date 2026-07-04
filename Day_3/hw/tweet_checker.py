text=str(input("Enter Your tweet: "))
print(len(text))
if len(text)==0:
    print("Empty String is Falsy")
elif len(text)<=280:
    print(f"Good To Post! ({len(text)}/280 chars)")
else:
    print(f"Your tweet is over by {len(text)-280} characters , Dont post ")
