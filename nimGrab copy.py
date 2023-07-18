# Akhil Pallem             9-26-22
# Assignment 3

# HINT: Explore the random library documentation to find a function that returns an integer within a specific range a <= N <= c
# https://docs.python.org/3/library/random.html
import random 

print("Welcome to NIMGRAB!")
print()

# TODO: Have student print their name/ section when the script runs
print("By: Akhil Pallem")
print("[COM S 127 A]")
print()

# Constant values
NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3

# Game flow variables
gameOver = False
currentTurn = 0 # 0 = human, 1 = computer NOTE: Alternate between turns 0 and 1 to play the game
while gameOver == False:
    choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
    print()
    if choice == "p":
        number = random.randint(NUM_ITEMS_LOW, NUM_ITEMS_HIGH)
        while number > 0:
            if currentTurn == 0:
                print("HUMAN TURN")
                print("They're currently " + str(number) +" items")
                counter = 0 
                while counter < number:
                    print(end="| ")
                    counter = counter + 1
                print(" ")
                humannum = int(input("How many will you take (1-3): "))
                while humannum != 1 and humannum != 2 and humannum != 3:
                    print("Enter a valid number from 1-3")
                    humannum = int(input("How many will you take (1-3): "))
                if humannum == 1 or humannum == 2 or humannum == 3:
                    print("The human has taken " + str(humannum) + " item(s)")
                    print(" ")
                number = number - humannum
            elif currentTurn > 0:
                print("COMPUTER TURN")
                print("They're currently " + str(number) +" item(s)")
                counter = 0 
                while counter < number:
                    print(end="| ")
                    counter = counter + 1
                print(" ")
                computernum = random.randint(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH)
                if number == 1:
                    computernum = 1
                elif computernum == 1 or computernum or 2 or computernum == 3:
                    while computernum == number or computernum > number:
                        computernum = random.randint(NUM_TO_TAKE_LOW, NUM_TO_TAKE_HIGH)
                print("The computer has taken " + str(computernum) + " items")
                print(" ")
                number = number - computernum
            currentTurn += 1
            currentTurn %= 2
            if number <= 0:
                if currentTurn == 0:
                    print("The computer has taken the last item... Therefore, the HUMAN has one")
                else:
                    print("The human has taken the last item... Therefore, the COMPUTER has won")
                    currentTurn = 0 
    elif choice == "i":
        print("Each player, the human and the computer, take turns removing objects from a pool.")
        print("Each player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total.")
        print("The game progresses until the last item is removed from the pool.")
        print("The player to take the last item loses the game.")
    elif choice == "q":
        print("Goodbye...")
        break
    else:
        print("Please enter [p], [i], or [q]...")
    
# initial loop tasks ------------------------------------------------------------------------------------------------------------------------
# TODO: create a main 'while loop' that executes as long as the gameOver variable is set to 'False'.

# TODO: within this main 'while loop,' create a call to the 'input' function that asks players if they want to "[p]lay, [i]nstructions, or [q]uit?: " and assign the output to a variable.

# TODO: within the main 'while loop,' create an if/ elif block that executes each section depending on the player's choice.
# EXAMPLE: if the player chooses "p", the "p" section should play the game. If the player chooses "q", the game should quit.

# TODO: add an 'else' case to the if/ elif block within the main 'while loop' that tells players to "Please enter [p], [i], or [q]..." if they enter a wrong initial choice.

# ---------------------------------------------------------------------------------------------------------------------------------------------

# "p" section tasks ------------------------------------------------------------------------------------------------------------------------

# TODO: within the "p" section of the if/ elif block inside the main while loop, use the 'random' library to select a value between NUM_ITEMS_LOW and NUM_ITEMS_HIGH and assign this value to a variable. This is the number of items in the item pool.

# HINT: Explore the random library documentation to find a function that returns an integer within a specific range a <= N <= c
# https://docs.python.org/3/library/random.html

# TODO: create a new 'gameplay' 'while loop' within the "p" section, after the 'number of items' variable is set. This loop will run while the 'number of items' is strictly greater than zero.

# TODO: within the 'gameplay' 'while loop', check to see if currentTurn is zero (0). If it is, it is the human's turn. If it is not, it is the computer's turn. Create an if/ else statement that reflects these two states.

# HUMAN's TURN STATE ------------------

# TODO: inside the 'human's turn' state, print out "HUMAN TURN:". Then print the number of items currently in the item pool.

# TODO: initialize a counter variable to zero (0), and use it in a new 'item drawing' 'while loop'. This 'item drawing' 'while loop' should print a character representing each item in the item pool. 
# EXAMPLE: If there are five (5) items in the item pool, you would draw: "| | | | | " where "| " represents the item.
# HINT: use end="" inside the print() function to prevent the computer from printing to a new line with each iteration of the loop/
# HINT: once the loop is finished, print a blank line with a call to 'print()' once all the items in the item pool are printed.

# TODO: take in input from the human player for the number of items the human wishes to take (between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH) and assign this value to a variable.
# TODO: perform input validation to ensure that the human enters an integer number, and that this number is between the range of NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH.
# HINT: consult the slide decks from week 5 where we did exactly this.

# TODO: print out that the human has taken the number of items that was input from before.

# TODO: subtract the number of items the human took from the number of items in the item pool.

# COMPUTER's TURN STATE ------------------

# TODO: inside the 'computer's turn' state, print out "COMPUTER TURN:". Then print the number of items currently in the item pool.

# TODO: initialize a counter variable to zero (0), and use it in a new 'item drawing' 'while loop'. This 'item drawing' 'while loop' should print a character representing each item in the item pool. 
# EXAMPLE: If there are five (5) items in the item pool, you would draw: "| | | | | " where "| " represents the item.
# HINT: use end="" inside the print() function to prevent the computer from printing to a new line after each iteration of the loop
# HINT: once the loop is finished, print a blank line with a call to 'print()' once all the items in the item pool are printed.

# TODO: generate a random number for the number of items the computer wishes to take (between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH) and assign this value to a variable.

# TODO: make sure that the computer does not accidentally take the last item when there is more than one item left. Meaning, if there are three (3) items left, and the computer randomly generates a three (3), it should choose something else instead.
# HINT: check if the number of items in the item pool is greater than one
# HINT: if the number of items in the item pool is greater than one, use a 'while loop' that executes while the number of items to take is greater than the number of items in the pool. If it is, then generate a new random number between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH and assign this value to the 'number to take' variable.
# HINT: if the number of items in the items pool is exactly one, then set the 'number to take' variable to be one (1). 

# TODO: print out that the computer has taken the number of items that was generated from before.

# TODO: subtract the number of items the computer took from the number of items in the item pool.

# SWITCH TURNS ------------------

# TODO: outside the if/ else statement that represents what happens during the human's/ computer's turn, at the same indentation level as this if/ else statement, add one (1) to the currentTurn.

# TODO: after adding one (1) to the current turn, apply one of the 'compound assignment operators' to the currentTurn variable, with the number of players as the right hand side operand.
# HINT: in this case, the number of players is two (2) - the human and the computer.
# HINT: options for the compound operator include: +=, -=, *=, /=, %=, and //= One of these operators will make the currentTurn variable alternate between 0 and 1.
# EXAMPLE: the formula is: currentTurn <compound operator> 2 
# EXAMPLE: the above formula equates to: currentTurn = currentTurn <arithmetic operator> 2

# ENDING THE GAME ------------------

# NOTE: when the number of items in the item pool is less than or equal to zero, it is time to determine who won and who lost

# NOTE: if the currentTurn variable is equal to zero (0) at this stage, that means that before this it was the computer's turn and then the currentTurn variable was incremented and adjusted to be in the range of 0 to 1. Similarly, if the currentTurn variable is equal to one (1) at this stage, that means that before this it was the human's turn and then the currentTurn variable was incremented and adjusted to be in the range of 0 to 1.

# TODO: create a new 'if/ else' statement at the same indentation level as the 'gameplay' 'while loop'. This is one indentation level in from the "p" choice 'if' statement. If currentTurn is equal to zero, print out that "The COMPUTER has taken the last item... Therefore, the HUMAN Has Won!" as per the logic in the NOTE above. Alternatively, if currentTurn does not equal zero (0), meaning it equals one (1), then print out "The HUMAN has taken the last item... Therefore, the COMPUTER Has Won!"

# TODO: outside the 'if/ else' statement create above, set currentTurn to be zero (0). This will be at the same indentation level as the 'if/ else' statement and the 'gameplay' 'while loop'. This will ensure that the human will always go first in the event they start a new game.

# ---------------------------------------------------------------------------------------------------------------------------------------------

# "i" section tasks ------------------------------------------------------------------------------------------------------------------------

# TODO: within the "i" section of the if/ elif block inside the main while loop, print out the instructions for the game.
# HINT: The instructions of the game are thus:
# Each player, the human and the computer, take turns removing objects from a pool. 
# Each player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total.
# The game progresses until the last item is removed from the pool.
# The player to take the last item loses the game.

# ---------------------------------------------------------------------------------------------------------------------------------------------

# "q" section tasks ------------------------------------------------------------------------------------------------------------------------

# TODO: within the "q" section of the if/ elif block inside the main while loop, set the gameOver variable to be 'True' and print a 'goodbye' message to the player