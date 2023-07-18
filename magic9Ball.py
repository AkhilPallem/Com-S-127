# Akhil Pallem            September 12th, 2022
# Assignment 2 

print("Welcome to the Magic 9 Ball...")
print()

print("By: Akhil")
print("[COM S 127 A]")
print()

print("What would you like to do?")
print()
choice = input("[c]alculator, [p]rediction, [q]uit: ")

if choice != "c" and choice != "p" and choice != "q":
    print("Enter a valid choice next time")
elif choice == "c":
    calc = input("What calculation? {+, -, %, /, **, *}: ")
    if calc != "+" and calc != "-" and calc != "%" and calc != "/" and calc != "**" and calc != "*":
        print("You must enter a valid operator")
    elif calc == "+":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 + num2
        print("Adding the numbers together gets you: " + str(final))
    elif calc == "%":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 % num2
        print("Modding the numbers together gets you: " + str(final))
    elif calc == "-":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 - num2
        print("Subtracting the numbers gets you: " + str(final))
    elif calc == "*":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 * num2
        print("Multiplying the numbers together gets you: " + str(final))
    elif calc == "/":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 / num2
        print("Dividing the numbers gets you: " + str(final))
    elif calc == "**":
        num1 = int(input("Enter an integer: "))
        num2 = int(input("Enter an integer: "))
        final = num1 ** num2
        print("Squaring the numbers gets you: " + str(final))
elif choice == "p":
    question = input("What is your question?: ")
    length = len(question)
    prediction_value = length % 10
    if prediction_value == 0:
        print("As for: " + question + " ...I predict it is not looking too good")
    elif prediction_value == 1:
        print("As for: " + question + " ...I predict it will rain")
    elif prediction_value == 2:
        print("As for: " + question + " ...I predict it will end up well")
    elif prediction_value == 3:
        print("As for: " + question + " ...I think you should go")
    elif prediction_value == 4:
        print("As for: " + question + " ...I predict it will be a good decision")
    elif prediction_value == 5:
        print("As for: " + question + " ...I predict it will likely go well")
    elif prediction_value == 6:
        print("As for: " + question + " ...I predict it wil end badly")
    elif prediction_value == 7:
        print("As for: " + question + " ...I predict you should NOT do that")
    elif prediction_value == 8:
        print("As for: " + question + " ...I predict an injury is coming")
    elif prediction_value == 9:
        print("As for: " + question + " ...I predict a bat to the head will end your career")
    elif prediction_value == 10:
        print("As for: " + question + " ...I predict you should")
elif choice == "q":
    print("Maybe next time...")