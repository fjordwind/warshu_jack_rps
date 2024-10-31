import random
from enum import Enum
import os

# choices for the classic mode
class Choice(Enum):
    SLATE = 1 ##slate
    PARCHMENT = 2 ##parchment
    CLEAVER = 3 ##cleaver

def playerChoice():
    while True:
        ##ask the player for their input
        userInput = input("Input your move:\n ---> ")
        if userInput.upper() in [choice.name for choice in Choice]:
            return Choice[userInput.upper()]
        elif userInput == "gun":
            print("Funny guy, but no.")
            continue
        else:
            print("Invalid choice, you have another chance.")
            continue

        
def cpuChoice():
    return random.choice(list(Choice))

def winningPlayer(playerChoice, cpuChoice):
    listOfWinners = {
        (Choice.SLATE, Choice.CLEAVER): "USER",
        (Choice.PARCHMENT, Choice.SLATE): "USER",
        (Choice.CLEAVER, Choice.PARCHMENT): "USER",
        (Choice.SLATE, Choice.SLATE): "NOBODY",
        (Choice.CLEAVER, Choice.CLEAVER): "NOBODY",
        (Choice.PARCHMENT, Choice.PARCHMENT): "NOBODY",
    }
    return listOfWinners.get((playerChoice, cpuChoice), "WARSHU")\

def rematchGame():
    while True:
        rematch = input("Battle once more?(Y/N)\n ----> ")
        if rematch == "y":
            playClassicGame()
        if rematch == "n":
            break

def playClassicGame():
    print("Plan out your odds, your choices are slate, parchment, and cleaver.")
    player_choice = playerChoice()
    warshus_choice = cpuChoice()
    victor = winningPlayer(player_choice,warshus_choice)
    print(F"You have decided {player_choice.name} against Warshu Jack's {warshus_choice.name}. {victor} is victorious.")
    rematchGame()
    
playClassicGame()
