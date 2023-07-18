# Matthew Holman             8-11-2022
# Assignment #6 Naval Battle

import random

GAME_BOARD_WIDTH = 10
GAME_BOARD_HEIGHT = 10

BOARD_SELECTION_LOW = 1
BOARD_SELECTION_HIGH = 2

def chooseHumanGameBoard():
    """This function allows the player to select which game board to use in the game. The player can always make more gameboards
    by typing them into a .txt file. All the gameboards should be numbered sequentially, with no 'gaps' in the numbering.

    Returns:
        int: gameboardChoice is an integer indicating which gameboard to load. For example, if gameboardChoice == 3, then the 
        script will load board3.txt
    """
    while True:
        try:
            gameboardChoice = int(input("Which gameboard to use for the player (" + str(BOARD_SELECTION_LOW) + " - " + str(BOARD_SELECTION_HIGH) + ")?: "))
            while gameboardChoice < BOARD_SELECTION_LOW or gameboardChoice > BOARD_SELECTION_HIGH:
                print("Invalid input...")
                gameboardChoice = int(input("Which gameboard to use for the player (" + str(BOARD_SELECTION_LOW) + " - " + str(BOARD_SELECTION_HIGH) + ")?: "))
            break
        except Exception as e:
            print("ERROR: chooseGameBoard - please enter an integer:", e)
            continue

    return gameboardChoice

def chooseComputerGameBoard():
    """This function has the computer randomly select a gameboard.

    Returns:
        int: gameboardChoice is an integer indicating which gameboard to load. For example, if gameboardChoice == 3, then the 
        script will load board3.txt
    """
    gameboardChoice = random.randint(BOARD_SELECTION_LOW, BOARD_SELECTION_HIGH)

    return gameboardChoice

def loadGameBoard(gameboardChoice):
    """This function loads a gameBoard file. It can be used for either the human or the computer.

    Args:
        gameboardChoice (int): The gameBoard files are named boardX.txt. This value indicates what the 'X' is.

    Returns:
        list of lists, int: gameBoard is a list of lists containing the data from the file. It contains all of the
        ship locations - designated by '@' characters. numTargets is the number of characters in the file that contain 
        an '@' character.
    """
    # load gameboard from file
    with open("board" + str(gameboardChoice) + ".txt", "r") as f:
        contents = f.readlines()
    
    gameBoard = []
    for line in contents:
        line = list(line)
        gameBoard.append(line[:len(line)-1])
    
    numTargets = 0
    for row in gameBoard:
        for character in row:
            if character == "@":
                numTargets += 1
    
    return gameBoard, numTargets

def loadTargetBoard():
    """This function loads the 'target board' which the human will use to track where they have attacked against the computer.

    Returns:
        list of lists: targetBoard is a list of lists containing the data from the file. It should contain all '#' characters.
    """
    # load targetboard from file
    with open("targetBoard.txt", "r") as f:
        contents = f.readlines()
    
    targetBoard = []
    for line in contents:
        line = list(line)
        targetBoard.append(line[:len(line)-1])
    
    return targetBoard

def printBoard(board, boardWidth, boardHeight):
    """This function prints out a specified game board to the terminal. It works for both computer/ human gameboards and the target board.

    Args:
        board (list of lists): Contains all of the data of a specific board.

        boardWidth (int): This is how many spaces wide the board is.

        boardHeight (int): This is how many spaces high the board is
    """
    colCoordinates = " "

    for i in range(0, boardWidth):
        colCoordinates += str(i)
    print(colCoordinates)
    for i in range(0, boardHeight):
        row = str(i)
        for j in range(0, boardWidth):
            row += board[i][j]
        print(row)

    return