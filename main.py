import random

print("welcome to the game Rock Predictor in the cup\n Pick a cup")
a = int(input("what's your choice: '0' or '1' or '2' "))

flip = random.randint(0, 2)

print(flip)

if (flip == a) and (a <= 2) :
    print("hurray! you won")
elif (a >= 2):
    print("enter a Valid Number")
else:
    print("sorry you lost, better luck next time")