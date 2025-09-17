import random
userWin = 0
computerWin = 0
opction = ["rock", "paper", "scissor"]
while True:
    userInput = input("Type rock paper scissor or Q to quit: ").lower()
    if userInput == "q":
        print("Okay")
        break
    if userInput not in opction:
        continue

    randomNumber = random.randint(0, 2)
    computerPick = opction[randomNumber]
    print("Computer pick", computerPick)


    if userInput == "rock" and computerPick == "scissor":
        print("You win!")
        userWin += 1
    elif userInput == "paper" and computerPick == "rock":
        print("You win!")
        userWin += 1
    elif userInput == "scissor" and computerPick == "paper":
        print("You win!")
        userWin += 1
    elif userInput == "rock" and computerPick == "rock":
        print("Draw!")
    elif userInput == "paper" and computerPick == "paper":
        print("Draw!")
    elif userInput == "scissor" and computerPick == "scissor":
        print("Draw!")
    else:
        print("Computer win!")
        computerWin += 1
        
print("You win", str(userWin), "times.")
print("And computer win", str(computerWin), "times.")