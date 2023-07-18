#Akhil Pallem    9-12-2022 
#Lab week 4      Exercise3
import math

x1 = float(input("Input a float for x1: "))
x2 = float(input("Input a float for x2: "))
y1 = float(input("Input a float for y1: "))
y2 = float(input("Input a float for y2: "))
if x2 - x1 == 0:
    print("The line described by the points (" + str(x1) + ", " + str(y1) + ") \
and (" + str(x2) + ", " + str(y2) + ") is a vertical line")
elif (y2 - y1) / (x2 - x1) == 0:
    slope = (y2 - y1) / (x2 - x1)
    print("The line described by the points (" + str(x1) + ", " + str(y1) + ") \
and (" + str(x2) + ", " + str(y2) + ") is a horizontal line")
else:
    slope = (y2 - y1) / (x2 - x1)
    print("The line described by the points (" + str(x1) + ", " + str(y1) + ") \
and (" + str(x2) + ", " + str(y2) + ") have a slope of: " + str(slope))

