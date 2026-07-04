Symbols=set("!@#$%^&*()_-+={}[]:;,.<>/")
def check_password(pw,min_length=8):
    score=0
    if len(pw)>= min_length:
        score+=1
    if any(ch.isdigit() for ch in pw):
        score+=1
    if any(ch.isupper() for ch in pw):
        score+=1
    if any(ch in Symbols for ch in pw):
        score+=1

    if score>=4:
        return "strong"
    elif score>=2:
        return "medium"
    return"weak"
pw = input("Choose a password: ")
print(f"Default rules (>=8) : {check_password(pw)}")
print(f"Strict rules (>=12) : {check_password(pw, min_length=12)}") 
    