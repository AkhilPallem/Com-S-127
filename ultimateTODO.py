# Akhil Pallem            11-7-22
# Assignment 5 

import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for k, v in todoList.items():
        if item in v:
            itemFound = True 
            keyName = k
            print("The item is already in the list! ")
            print()
            break 
        else:
            return itemFound, keyName, index
    
    return itemFound, keyName, index

def addItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if not itemFound:
        todoList["backlog"].append(item)
    return todoList

def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound:
        todoList[keyName].pop(index)

    return itemFound, todoList

def moveItem(item, todoList, new_list):
    deleteItem(item, todoList)
    todoList[new_list].append(item)
    print()
    
    return todoList

def printTODOList(todoList):
    for key, value in todoList.items():
        print(key, ":", value)
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()
        if choice == "a":
            item = input("Enter an item add: ")
            addItem(item, todoList)
            printTODOList(todoList)
        elif choice == "m":
            item = input("Enter an item to move: ")
            print()
            new_list = input("What list would you like to add it to?: ")
            moveItem(item, todoList, new_list)
            printTODOList(todoList)
            pass
        elif choice == "d":
            item = input("Enter an item to delete: ")
            deleteItem(item, todoList)
            printTODOList(todoList)
            pass
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
        elif choice == "q":
            print("Returning to MAmIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    # TODO: Have student print their name/ section when the script runs (0.5 pt.)
    print("By: Akhil Pallem")
    print("[COM S 127 A]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()