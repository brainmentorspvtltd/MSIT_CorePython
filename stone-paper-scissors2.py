import random
gameChoices = ["stone", "paper", "scissors"]
userWins = 0
cpuWins = 0
gameDraw = 0

while userWins < 3 and cpuWins < 3:
    print('''
        1. Stone
        2. Paper
        3. Scissors
    ''')
    userInput = int(input("User turn: "))
    print("User entered:", gameChoices[userInput - 1])
    if userInput > 3 or userInput < 1:
        continue
    else:
        cpuInput = random.randint(1, 3)
        print("CPU turn:", gameChoices[cpuInput - 1])

        if userInput == cpuInput:
            print("Game draw")
            gameDraw += 1
        elif userInput == 1:
            if cpuInput == 2:
                print("CPU wins")
                cpuWins += 1
            else:
                print("Player wins")
                userWins += 1
        elif userInput == 2:
            if cpuInput == 3:
                print("CPU wins")
                cpuWins += 1
            else:
                print("Player wins")
                userWins += 1
        else:
            if cpuInput == 1:
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
