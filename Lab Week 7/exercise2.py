#Akhil Pallem 
#Section A        10-3-22
number = int(input("Enter an integer: "))
for i in range(0, number):
    for j in range(0, i + 1):
        print(j, end="")
    print()
