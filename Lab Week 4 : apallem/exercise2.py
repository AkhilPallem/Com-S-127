#Akhil Pallem    9-12-2022 
#Lab week 4      Exercise2
import math 

a = float(input("Input a float for a: "))
b = float(input("Input a float for b: "))
c = float(input("Input a float for c: "))
x = float(input("Input a float for x: "))
y = float(input("Input a float for y: "))
point = a * x ** 2 + b * x + c 
if y == point: 
    print("The point (" + str(x) + ", " + str(y) + ") lies on the parabola\
 described by the equation: y = " + str(a) + " * " + str(x) + " ** 2 + " + str(b) + " * \
" + str(x) + " + " + str(c))
else: 
    print("The point (" + str(x) + ", " + str(y) + ") does not lie on the parabola\
 described by the equation: y = " + str(a) + " * " + str(x) + " ** 2 + " + str(b) + " * \
" + str(x) + " + " + str(c))