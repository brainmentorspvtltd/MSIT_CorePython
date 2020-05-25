import random
gameChoices = ["stone", "paper", "scissors"]
userWins = 0
cpuWins = 0
gameDraw = 0

while userWins < 3 and cpuWins < 3:
    userInput = input("User turn: ")
    if userInput not in gameChoices:
        continue
    else:
        cpuInput = random.choice(gameChoices)
        print("CPU turn:", cpuInput)

        if userInput == cpuInput:
            print("Game draw")
            gameDraw += 1
        elif userInput == "stone":
            if cpuInput == "paper":
                print("CPU wins")
                cpuWins += 1
            else:
                print("Player wins")
                userWins += 1
        elif userInput == "paper":
            if cpuInput == "scissors":
                print("CPU wins")
                cpuWins += 1
            else:
                print("Player wins")
                userWins += 1
        else:
            if cpuInput == "stone":
                print("CPU wins")
                cpuWins += 1
            else:
                print("Player wins")
                userWins += 1

    print(
        f"Score -> User : {userWins}, CPU : {cpuWins}, Draw : {gameDraw}, Total Matches : {userWins + cpuWins + gameDraw}")

# someVariableName -> camelcase
# stone -> paper
# stone -> scissors
# paper -> stone -> user
# paper -> scissors -> cpu
# scissors -> stone -> cpu
# scissors -> paper -> user
