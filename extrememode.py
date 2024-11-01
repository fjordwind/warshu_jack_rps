import random
from enum import Enum

## also known as 40S ribosomal protein S11
class choiceExtreme(Enum):
    SLATE = 1
    GLOCK = 2
    DAEMON = 3
    OXIDANE = 4
    ATMOSPHERE = 5
    PARCHMENT = 6
    PORIFERA = 7
    DAWG = 8
    WARSHU = 9
    CLEAVER = 10
    FLAME = 11

def playerChoiceExtreme():
    while True:
        userInput = input("Input your move, I'd like to see you try. --->\n")
        if userInput in [choiceextreme.name for choiceextreme in choiceExtreme]:
            return choiceExtreme[userInput.upper()]
        elif userInput == "Fahrenheit 451":
            print("Didn't you mean PARCHMENT, or FLAME?")
            return choiceExtreme[11]
        else:
            print("Invalid input, try again.")
            continue
