# Akhil Pallem            October 24th
# Assignment 4 

import random
import sys

# GLOBAL CONSTANT VARIABLES
START_ROOM = 1
FINAL_ROOM = 9999

def combat(combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage):
    enemyName = ""
    enemyHealth = 0
    enemyAccuracy = 0
    enemyDamage = 0
    # Check to see if we should engage in combat
    if combatChance > random.randint(0, 9):
        print("You have engaged in combat!")
        print()

        # Randomly select an enemy
        monsterSelection = random.randint(0, 0)
        if monsterSelection == 0: # SLIME monster
            enemyName = "SLIME"
            maxEnemyHealth = 2
            enemyHealth = maxEnemyHealth
            enemyAccuracy = 5
            enemyDamage = 1
            print("You have encountered an enemy {0} monster...".format(enemyName))
            print()
            print("It has {0} HP and {1} ATTACK strength...".format(enemyHealth, enemyDamage))
            print()
        else:
            print("Error - 'combat' function: 'monsterSelection' value is invalid:", monsterSelection)

        # Choose a random turn to go first
        currentTurn = random.randint(0, 1)
        if currentTurn == 0:
            print("You have taken the initiative!")
        else:
            print("The enemy {0} monster has struck first!".format(enemyName))
        print()

        # Take turns
        while playerHealth > 0 and enemyHealth > 0:
            if currentTurn == 0: # Human Turn
                # Get the action the human wants to take
                action = input("COMBAT: [a]ttack, [f]lee: ")
                while action != "a" and action != "f":
                    print("Invalid combat choice...")
                    action = input("COMBAT: [a]ttack, [f]lee: ")
                print()

                # Engage in combat depending on the action
                if action == "a":
                    if random.randint(0, 9) < playerAccuracy:
                        enemyHealth -= playerDamage
                        print("You have HIT the enemy monster! Its HP is: {0} / {1}".format(enemyHealth, maxEnemyHealth))
                        print()
                    else:
                        print("You have MISSED the enemy monster...")
                        print()
                elif action == "f":
                    if random.randint(0, 9) < playerDamage:
                        print("You have escaped from combat!")
                        print()
                        break
                else:
                    print("Error - 'combat' function: 'action' value is invalid:", action)

            else: # Computer Turn 
                if random.randint(0, 9) < enemyAccuracy:
                    playerHealth -= enemyDamage
                    print("You have been HIT by the the enemy {0} monster! Your HP is: {1} / {2}".format(enemyName, playerHealth, maxHealth))
                    print()
                else:
                    print("The enemy {0} monster has MISSED you...".format(enemyName))
                    print()
            # switch turns
            currentTurn += 1
            currentTurn %= 2
        
        # Announce the winner
        if playerHealth > 0 and enemyHealth <= 0:
            print("Congratulations! You have defeated the enemy {0} monster...".format(enemyName))
            print()
        elif playerHealth > 0 and enemyHealth > 0:
            print("That was a close one! The enemy {0} monster almost got you!".format(enemyName))
            print()
        else:
            print("Sadly, the enemy {0} monster was victorious...".format(enemyName))
            print()
    else:
        print("Fortunately, there were no monsters in this room...")
        print()
    
    return playerHealth

# Functions to represent dungeon rooms
# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room1(goldAmount, visited_room, playerHealth, maxHealth, playerAccuracy, playerDamage, combatChance):
    if visited_room == False:
        gold = 10 # This is the amount of gold the room contains.
        print("Welcome to your first room in the dungeon...goodluck with your journey. May not of been so wise coming here...but only time will tell.")
        combat(combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print() 

        # Mark the room as 'visited'
        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    movement()


def movement():
    direction = input("[1] [2] [3] [4] [5] [6]?: ")
    while direction != "1" and direction != "2" and direction != "3" and direction != "4" and direction != "5" and direction != "6" and direction != "F":
        print("Invalid input...")
        direction = input("[1] [2] [3] [4] [5] [6]?: ")
    if direction == "1":
        currentRoom = 1
    elif direction == "2":
        currentRoom = 2
    elif direction == "3":
        currentRoom = 3
    elif direction == "4":
        currentRoom = 4
    elif direction == "5":
        currentRoom = 5
    elif direction == "6":
        currentRoom = 6
    elif direction == "F":
        currentRoom = FINAL_ROOM
    # roomChoice = -1 # HINT: Once this section is encapsulated into a function, it would be wise to have a default roomChoice value outside that function.
    # if direction == "1":
    #     roomChoice = 1
    # elif direction == "2":
    #     roomChoice = 2
    # elif direction == "3":
    #     roomChoice = 3
    # elif direction == "4":
    #     roomChoice = 4
    # elif direction == "5":
    #     roomChoice = 5
    # elif direction == "6":
    #     roomChoice = 6
    # elif direction == "F":
    #     roomChoice = FINAL_ROOM
        
    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return currentRoom

# NOTE: You can change the number/ order of parameters being used in your room functions to fit the needs of your game.
def room2(goldAmount, visited_room):
    if visited_room == False:
        print("ROOM 2 EMANUEL")
        gold = 20 # This is the amount of gold the room contains.
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    movement()
    return goldAmount, visited_room
    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    """
    direction = input("[1] [3] [4] [5] [6]?: ")
    while direction != "1" and direction != "3" and direction != "4" and direction != "5" and direction != "6":
        print("Invalid input...")
        direction = input("[1] [3] [4] [5] [6]?: ")
    
    roomChoice = 2 
    if direction == "1":
        roomChoice = 1
    elif direction == "3":
        roomChoice = 3
    elif direction == "4":
        roomChoice = 4
    elif direction == "5":
        roomChoice = 5
    elif direction == "6":
        roomChoice = 6
    """

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    # return roomChoice, goldAmount, visited_room

def room3(goldAmount, visited_room):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    print("room 3")
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()

    # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    # direction = input("[1] [2] [4] [5] [6]?: ")
    # while direction != "1" and direction != "2" and direction != "4" and direction != "5" and direction != "6":
    #     print("Invalid input...")
    #     direction = input("[1] [2] [4] [5] [6]?: ")
    
    # roomChoice = 3 
    # if direction == "1":
    #     roomChoice = 1
    # elif direction == "2":
    #     roomChoice = 2
    # elif direction == "4":
    #     roomChoice = 4
    # elif direction == "5":
    #     roomChoice = 5
    # elif direction == "6":
    #     roomChoice = 6

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return goldAmount, visited_room


def room4(goldAmount, visited_room, playerHealth, maxHealth, playerAccuracy, playerDamage, combatChance):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.
        print("As you approach this room you sense a disturbance...")
        combat(combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    movement()
    # # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    # direction = input("[1] [2] [3] [5] [6]?: ")
    # while direction != "1" and direction != "2" and direction != "3" and direction != "5" and direction != "6":
    #     print("Invalid input...")
    #     direction = input("[1] [2] [3] [5] [6]?: ")
    
    # roomChoice = 4
    # if direction == "1":
    #     roomChoice = 1
    # elif direction == "2":
    #     roomChoice = 2
    # elif direction == "3":
    #     roomChoice = 3
    # elif direction == "5":
    #     roomChoice = 5
    # elif direction == "6":
    #     roomChoice = 6

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return goldAmount, visited_room


def room5(goldAmount, visited_room, playerHealth, maxHealth, playerAccuracy, playerDamage, combatChance):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.
        print("You sense your getting closer...but not quite out yet...")
        combat(combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    movement()
    # # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    # direction = input("[1] [2] [3] [4] [6]?: ")
    # while direction != "1" and direction != "2" and direction != "3" and direction != "4" and direction != "6":
    #     print("Invalid input...")
    #     direction = input("[1] [2] [3] [4] [6]?: ")
    
    # roomChoice = 5
    # if direction == "1":
    #     roomChoice = 1
    # elif direction == "2":
    #     roomChoice = 2
    # elif direction == "3":
    #     roomChoice = 3
    # elif direction == "4":
    #     roomChoice = 5
    # elif direction == "6":
    #     roomChoice = 6

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return goldAmount, visited_room


def room6(goldAmount, visited_room):
    # NOTE: If your room uses a shop/ combat function, it should likely be placed at the top of the room function it appears in.

    # NOTE: Replace this portion of code with the 'room visited'/ 'gold amount' function created in the 'room1' function above.
    if visited_room == False:
        gold = 20 # This is the amount of gold the room contains.

        print()
        print("The room has", gold, "gold pieces in it...")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
        print()

        visited_room = True
    else:
        print()
        print("You have already visited this room before...")
        print()
    movement()
    # # NOTE: Replace this code before the 'return' statement with the 'direction' function created in the 'room1' function above.
    # direction = input("[1] [2] [3] [5] [6]?: ")
    # while direction != "1" and direction != "2" and direction != "3" and direction != "4" and direction != "5":
    #     print("Invalid input...")
    #     direction = input("[1] [2] [3] [5] [6]?: ")
    
    # roomChoice = 6
    # if direction == "1":
    #     roomChoice = 1
    # elif direction == "2":
    #     roomChoice = 2
    # elif direction == "3":
    #     roomChoice = 3
    # elif direction == "4":
    #     roomChoice = 4
    # elif direction == "5":
    #     roomChoice = 5

    # NOTE: You can change the number/ order of variables being returned to fit the needs of your game.
    return goldAmount, visited_room

def final_room():
    print("After a long journey through the dungeon, you have escaped! Well done traveler!")


# Main function
def main():
    # Set to 'True' when the game is over.
    gameOver = False

    # Player status variables/ constants. 
    # HINT: If you have other player variables to use, such as health, damage, etc. add them here.
    START_GOLD = 0 # HINT: This is a 'constant' value. Notice how it is used to set/ reset the goldAmount value.
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False # HINT: Carefully study how these 'visited room' variables are used.
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    visited_room6 = False
    playerHealth = 20 
    maxHealth = 20 
    combatChance = 3
    playerAccuracy = 7 
    playerDamage = 6

    print("Welcome to Dungeon Crawl...")
    print()

    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Akhil Pallem")
    print("[COM S 127 A]")
    print()

    while gameOver == False:
        choice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": # (**"p" Section Tasks**)
            while currentRoom != FINAL_ROOM: # HINT: When implmenting combat, if the player's health is <= 0, this loop should not execute.
                if currentRoom == 1:
                    room1(goldAmount, visited_room1, combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
                elif currentRoom == 2:
                    room2(goldAmount, visited_room2, currentRoom)
                elif currentRoom == 3:
                    room3(goldAmount, visited_room3)
                elif currentRoom == 4:
                    room4(goldAmount, visited_room4, combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
                elif currentRoom == 5:
                    room5(goldAmount, visited_room5, combatChance, playerHealth, maxHealth, playerAccuracy, playerDamage)
                elif currentRoom == 6:
                    room6(goldAmount, visited_room6)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
            
            # HINT: If the player's health is > 0 when they escape the dungeon print a message like this one. 
            # Otherwise print a message stating that they perished in the dungeon.
            if playerHealth > 0:
                print()
                print("You have escaped with", goldAmount, "gold from the dungeon!")
                print()
            else:
                print("You have perished in the dungeon ")


            maxHealth = 20 
            combatChance = 5 
            playerAccuracy = 7 
            playerDamage = 6
            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
            visited_room6 = False
        elif choice == "i": # (**"i" Section Tasks**)
            print("Traverse the dangerous dungeon and try and find an exit alive...")
        elif choice == "q": # (**"q" Section Tasks**)
            gameOver = True 
            break
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()