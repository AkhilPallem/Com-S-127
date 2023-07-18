# Akhil Pallem 
# 9-26-22 
#Section A, Lab week 6, and Excercise2

counter1 = int(input("Enter an integer: "))
reset = int(input("Enter an integer: "))
while counter1 > 0:
    counter2 = reset 
    while counter2 > 0:
        print(counter1 * counter2, " ", end="")
        counter2 -= 1 
    print(" ")
    counter1 -= 1