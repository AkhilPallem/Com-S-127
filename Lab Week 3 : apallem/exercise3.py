# Akhil Pallem 9-7-2022 
#Lab week 3 - excersise3.py
import math 

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c. This cannot be zero or the same as variable a: "))

sum = a + b + c 
print("The sum of all 3 varaiables is: " + str(sum))

mod = a % c 
print("The modulus of varaible a and c is: " + str(mod))

final = (a * b) / c
print("Multiplying a and b then dividing by c, gets you: " + str(final))

average = (a + b + c) / 3 
print("The average of all 3 varaibles is: " + str(average))