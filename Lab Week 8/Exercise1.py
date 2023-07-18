#Akhil Pallem 
#10-10-22 
#Lab Week 8

def calc(x, y):
    counter = x
    for i in range(y - 1):
        x += counter
    print("The product of " + str(counter) + " x " + str(b) + " = " + str(x))

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
calc(a, b)