# Matthew Holman             8-11-2022
# Assignment #6 Naval Battle
import random
import gameBoard

def getHumanInput():
    """This function takes in input from the human for wich row and column they want to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the human to attack.
    """
    row = None 
    while row not in range(0, gameBoard.GAME_BOARD_WIDTH):
        try: 
            row = int(input("What row would you like to attack?: "))
        except ValueError:
            row = int(input("Not Valid! What row would you like to attack?: "))
        else:
            if row not in range(0, gameBoard.GAME_BOARD_WIDTH):
                row = int(input("Not Valid! What row would you like to attack?: "))
    

    col = None 
    while col not in range(0, gameBoard.GAME_BOARD_HEIGHT):
        try: 
            col = int(input("What column would you like to attack?: "))
        except ValueError:
            col = int(input("Not Valid! What column would you like to attack?: "))
        else:
            if col not in range(0, gameBoard.GAME_BOARD_HEIGHT):
                col = int(input("Not Valid! What column would you like to attack?: "))
    
    return row, col

def getComputerInput():
    """This function randomly generates input from the computer for which row and column it wants to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the computer to attack.
    """
    row = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)

    col = random.randint(0, gameBoard.GAME_BOARD_HEIGHT- 1)

    return row, col