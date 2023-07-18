# Akhil Pallem 9-7-2022 
#Lab week 3 - excersise5.py

print("Welcome to grade calculator. Enter 4 classes and the grades of each 4 and we'll calculate your average")
class1 = input("Enter class 1: ")
grade1 = int(input("Enter grade for class 1: "))

class2 = input("Enter class 2: ")
grade2 = int(input("Enter grade for class 2: "))

class3 = input("Enter class 3: ")
grade3 = int(input("Enter grade for class 3: "))

class4 = input("Enter class 4: ")
grade4 = int(input("Enter grade for class 4: "))

average = (grade1 + grade2 + grade3 + grade4) / 4
print("The average grade between " + class1 + ", " + class2 + ", " + class3 + ", and " + class4 + " is: " + str(average))