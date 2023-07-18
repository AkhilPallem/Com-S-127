#Akhil Pallem
#Assignment 7

"""
This program has the use pick the game they want to play using r or g.
It then executes the game choosen so the user can play.
For rock paper scissors...it keeps track of wins losses and ties 
For guess the number...It keeps track of how many guesses the user takes to finally guess the correct number
"""


import random 
def rock():
    play = True
    wins = 0 
    losses = 0 
    ties = 0 
    player = input("[r]ock, [p]aper, or [s]cissors?: ")
    print()
    while play == True: 
        computer = random.choice("rps")
        if player == "r" and computer == "r":
            print("You both picked rock. TIE")
            ties = ties + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "r" and computer == "p":
            print("You picked rock. Computer picked paper. COMPUTER WINS")
            losses = losses + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "r" and computer == "s":
            print("You picked rock. Computer picked scissors. YOU WIN")
            wins = wins + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "p" and computer == "r":
            print("You picked paper. Computer picked Rock. YOU WIN!")
            wins = wins + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "p" and computer == "p":
            print("You picked paper. Computer picked Paper. TIE")
            ties = ties + 1
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "p" and computer == "s":
            print("You picked paper. Computer picked scissors. COMPUTER WINS")
            losses = losses + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "s" and computer == "r":
            print("You picked scissors. Computer picked rock. COMPUTER WINS")
            losses = losses + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "s" and computer == "p":
            print("You picked scissors. Computer picked paper. YOU WIN")
            wins = wins + 1 
            print("WINS:", wins, " LOSSES:", losses, " TIES: ", ties)
            print()
        elif player == "s" and computer == "s":
            print("You picked scissors. Computer picked scissors. TIE")
            ties = ties + 1 
            print("WINS:", wins, "LOSSES:", losses, "TIES:", ties)
            print()
        play = input("Would you like to play again? [y]es or [n]o: ")
        print()
        if play == "y":
            play = True 
            player = input("[r]ock, [p]aper, or [s]cissors?: ")
            print()
        else:
            print("Byeeeee...you finished with... Wins:", wins, " losses:", losses, "ties:", ties)
            play = False 
    

def number():
    guesses = 0 
    number = random.randint(0, 999999999)
    guess = int(input("What random number do you think the computer has generated? "))
    print()
    while True:
        if guess > number: 
            print("Too high....try lower.....")
            print()
            guesses = guesses + 1 
            print("You have taken", guesses, "guesses so far")
            print()
            guess = int(input("What random number do you think the computer has generated? "))
        elif guess < number:
            print("Too low....try guessing higher next time")
            print()
            guesses = guesses + 1 
            print("You have taken", guesses, "guesses so far")
            print()
            guess = int(input("What random number do you think the computer has generated? "))
        elif guess == number:
            print("YOU GUESSED IT...the number was:", number, "It took you", guesses, "guesses")
            break 
    

def main():
    choice = input("What game would you like to play? [r]ock, paper, scissors or [g]uess the number: ")
    print()
    if choice == "r":
        rock()
    elif choice == "g":
        number ()


main()