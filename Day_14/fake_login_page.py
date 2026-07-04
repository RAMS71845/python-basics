# users={
#     "Ram Srivastava": "Ram@123"
# }
# attempts=3

# while attempts>0:
#     user_name=input("Enter your username: ")
#     password=input("Enter your password: ")

#     if user_name not in users:
#         print("Invalid username.Please Try Again")
#         break
#     if password==users[user_name]:
#         print("Login Successful!")
#         break

#     attempts-=1
#     if attempts==0:
#         print("Account Locked!")
#     else:
#         print(f"Wrong Password. Tries left:{attempts}")

#2nd way

class LoginSystem:
    def __init__(self,users,max_attempts=3):
        self.users=users
        self.max_attempts=max_attempts
        self.failed={}
        self.locked=set()

    def login(self,username,password):
        if username in self.locked:
            return "ACCOUNT LOCKED"
        if username not in self.users:
            return "No_USER"
        if self.users[username]==password:
            self.failed[username]=0 #saare uske past attempts ko 0 krdiya agr self.user mai milgya toh
            return 'OK'
        self.failed[username]=self.failed.get(username,0)+1
        if self.failed[username]>=self.max_attempts:
            self.locked.add(username)
            return "Account locked"
        return "Invalid password"
if __name__ == "__main__":
    users = {"RamSrivastava": "ram@123", "rahul": "hunter2"}
    system = LoginSystem(users, max_attempts=3)

    trials = [
        ("RamSrivastava", "ram@123"),
        ("RamSrivastava", "wrong"),
        ("rahul", "still-wrong"),
        ("rahul", "pass123"),
        ("rahul", "hunter2"),
        ("ghost", "any"),
    ]
    for username, pw in trials:
        print(f"login({username!r}, {pw!r}) -> {system.login(username, pw)}")
