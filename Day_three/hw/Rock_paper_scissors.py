import random
player=input("enter rock,paper or scissors: ").strip().lower()
if player not in["rock","paper","scissors"]:
    print("Invalid move!!")
else:
    computer=random.choice(["rock","paper","scissors"])


    print("Your choice: ",player)
    print("computer chose: ",computer)

    if player==computer:
        print("!!DRAW!!")

    elif (
        (player=="rock"and computer=="scissors")or
        (player=="paper"and computer=="rock")or
        (player=="scissors"and computer=="paper")
    ):
        print("you win!!")
    else:
        print("Computer wins!!!")