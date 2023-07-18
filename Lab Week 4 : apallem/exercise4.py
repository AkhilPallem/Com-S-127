#Akhil Pallem    9-12-2022 
#Lab week 4      Exercise4

import math 
m1 = float(input("Input a float for m1: "))
m2 = float(input("Input a float for m2: "))
angle = math.atan((m1 - m2) / (1 + m1 * m2))
if m1 == m2:
    print("The lines with slopes m1: " + str(m1) + " and m2: " + str(m2) + " are parallel")
elif m1 * m2 == -1:
    print("The lines with slopes m1: " + str(m1) + " and m2: " + str(m2) + " are perpendicular")
else:
    final = angle * 180 / math.pi 
    print("The angle is: " + str(final))
