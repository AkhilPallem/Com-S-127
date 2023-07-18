# Matthew Holman             8-11-2022
# Assignment #6 Naval Battle
import gameBoard
import gameInput

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    """This function controls what happens when it is the human's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numComputerTargets (int): The number of computer targets remaining.
    
    Returns:
        list of lists, list of lists, list of lists, int: All of the relevant gameboards and the number of computer targets remaining.
    """

    print("HUMAN TURN")
    print()
    gameBoard.printBoard(targetBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)
    gameBoard.printBoard(humanGameBoard, gameBoard.GAME_BOARD_WIDTH, gameBoard.GAME_BOARD_HEIGHT)

    while True:
        row, col = gameInput.getHumanInput()
        if targetBoard[row][col] == "X" or targetBoard[row][col] == "O":
            print("Invalid")
            break
    
    print("Coordinates attacked are row: " + str(row) + " and Column: " + str(col))
    
    if computerGameBoard[row][col] == "@":
        computerGameBoard[row][col] = "X"
        targetBoard[row][col] = "X"
        print("Hit")
        numComputerTargets -= 1 
    else:
        computerGameBoard[row][col] = "O"
        targetBoard[row][col] = "O"
        print("Miss")
    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
    """This function controls what happens when it is the computer's turn.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets remaining.
    
    Returns:
        list of lists, int: All of the relevant gameboards and the number of human targets remaining.
    """
    # TODO: Complete the logic below so that the computer can take a turn attacking the human. (1 pt.)

    # Print out that it's the computer's turn.
    print("COMPUTER TURN")
    print()

    while True:
        row, col = gameInput.getComputerInput()
        while humanGameBoard[row][col] != 'X' or humanGameBoard[row][col] != 'O':
            break

    # Print out the coordinates the computer is targeting.
    print("Computer is attacking coordinates row: " + str(row) + " and Column: " + str(col))

    if humanGameBoard[row][col] == '@':
        humanGameBoard[row][col] = 'X'
        print("HIT!")
        numHumanTargets -= 1    
    else: 
        humanGameBoard[row][col] = "O"
        print("MISS")
        print()
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    """This function prints out which player has won the game, depending on the numComputerTargets remaining.

    Args:
        numComputerTargets (int): The number of computer targets left. If there are none, the human wins. Else - the computer wins.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.
    """
    if numComputerTargets == 0:
        print("HUMAN WINS")
    else:
        print("COMPUTER WINS")
    
    gameBoard.printBoard(computerGameBoard)

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    """This function controls the flow of the game and switches turns between the human and the computer.

    Args:
        humanGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        targetBoard (list of lists): Contains the 'top part' of the gameboard - where the hits/ misses against the computer go. 
        Only the human needs one.

        computerGameBoard (list of lists): Contains the 'bottom part' of the gameboard - where the 'ships' are placed.

        numHumanTargets (int): The number of human targets left.

        numComputerTargets (int): The number of computer targets left.
    """
    currentTurn = 0 # 0 = human, 1 = computer


    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        currentTurn += 1
        currentTurn %= 2
    
    _printWinner(numComputerTargets, computerGameBoard)

    return