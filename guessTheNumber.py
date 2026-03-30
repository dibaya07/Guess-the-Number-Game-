import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target : "))
    if(userChoice == target):
        print("Success : Correct guess!!")
        break
    elif(userChoice < target):
        print("Target is bigger than this. Make a another Guess")
    else:
        print("Target is smaller than this. Make a another Guess")

print("----GAME OVER----")