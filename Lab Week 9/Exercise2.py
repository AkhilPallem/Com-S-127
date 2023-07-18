import math
#Akhil Pallem Lab week 9 
def main():
    listName = []
    listX = []
    listY = []
    for i in range(6):
        name = input("Enter a name (* to quit): ")
        if name == "*":
            x = int(input("Enter your X position: "))
            y = int(input("Enter your Y position: "))
            user_list = [x, y]
            break
        listName.append(name)
        x = int(input("Input X: "))
        y = int(input("Input Y: "))
        listX.append(x)
        listY.append(y)
    calculateDistance(x, y, listX, listY, listName, user_list)


def calculateDistance(x, y, listX, listY, listName, user_list):
    listDistances = []
    for i in range(len(listX)):
        listDistances.append(math.sqrt(((user_list[0] - listX[i]) ** 2) + ((user_list[1] - listY[i]) ** 2)))
    low = listDistances[0]
    number = 0 
    for i in range(len(listDistances)):
        if listDistances[i] < low:
            low = listDistances[i]
            number = i 
    print(listName)
    print(listDistances)
    print("The distance between " + listName[number] + " and my location (" + str(x) + " , "  + str(y) + ") is: " + str(low))

if __name__ == "__main__":
    main()

