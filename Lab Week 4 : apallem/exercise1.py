#Akhil Pallem 9-12-2022
#Lab exercise 1 
import math 

length = float(input("Enter a float for the length: "))
height = float(input("Enter a float for the heigth: "))
perimeter = 2 * (length * height)
if length == height: 
    print("The rectangle is a square with the perimeter of " + str(perimeter))
else:
    print("The rectangle is not a square and has a perimeter of " + str(perimeter))