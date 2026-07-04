import random
roll = random.randint(1,6)
print("You rolled :",roll)

print("Random pick",random.choice(["Rock","Paper","Scissors"]))

#create a coin flip
print("coin flipped : ",random.choice(["Heads","Tails"]))

#odd and even
game=random.randint(1,10)
print("LET's PLAY",game)



cards = ["Ace", "King", "Queen", "Jack", "10"]
random.shuffle(cards)
print("Shuffled cards:", cards)