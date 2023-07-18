# Akhil Pallem 9-7-2022 
#Lab week 3 - excersise2.py
import math

print("Lets find the area and volume of a sphere! Enter the radius below.")
radius = float(input("Enter the value of the radius: "))
area = 4 * math.pi * (radius ** 2)
volume = (4 * math.pi * (radius ** 3)) / 3
print("The area of the sphere is: " + str(area))
print("The volume of the sphere is: " + str(volume))
