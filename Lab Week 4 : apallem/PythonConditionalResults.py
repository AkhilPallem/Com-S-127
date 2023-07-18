#Akhil Pallem 9-12-2022
#Week 4 - Conditionals results 

#Question 1 
#Ouput will be "Computer's Answer: False" 
#Left is 335 and right is 131
x = 7
y = 12
if x * x * x + y == y * x + 47:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("x * x * x + y = {0}".format(x * x * x + y))
print("y * x + 47 = {0}".format(y * x + 47))

#Question 2 
#Output will be "Computer's Answer: True"
#Left is 152, Right is 180
x = 3
y = 4
z = 5
if 1000 * x / y / z + 2 <= x ** 2 * 20:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("1000 * x / y / z + 2 = {0}".format(1000 * x / y / z + 2))
print("x ** 2 * 20 = {0}".format(x ** 2 * 20))


#Question 3 
#Output will be "Computer's Answer: False"
#Left is 27, Right is 38
x = 12
y = 47
z = 3
if x + y // z >= x * z % y + 2:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("x + y // z = {0}".format(x + y // z))
print("x * z % y + 2 = {0}".format(x * z % y + 2))

#Question 4 
#Ouput will be "Computer's Answer: True"
#Left is 2, right is 8 
x = 8
y = 9
z = 10
if x * y % z != z % y * x:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")

print("x * y % z = {0}".format(x * y % z))
print("z % y * x = {0}".format(z % y * x))

#Question 5 
#Ouput will be "Computer's Answer: True"
#Left is 0, right is 0 
x = 3
y = x + 400 // 3 ** 2
z = x * y % 10 + 2 ** 2
if z * y ** 2 % 5 == z * 2 ** y % 4:
    print("Computer's Answer: True")
else:
    print("Computer's Answer: False")
print("z * y ** 2 % 5 = {0}".format(z * y ** 2 % 5))
print("z * 2 ** y % 4 = {0}".format(z * 2 ** y % 4))