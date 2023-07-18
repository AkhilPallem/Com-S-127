#Akhil Pallem 
#Section A        10-3-22
number = int(input("Enter an integer: "))
for i in range(number):
    for j in range (i + 1):
        print("*", end="")
    print("")
for l in range(number, 1, -1):
    for k in range(l, 1, -1):
        print("#", end="")
    print("")
