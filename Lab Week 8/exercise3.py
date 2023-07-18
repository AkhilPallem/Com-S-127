#Akhil Pallem 
#10-10-22 
#Lab Week 8 

def swap(a, b):
    letter = a 
    a = b 
    b = letter 
    return a, b

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
x, y = swap(a, b)
print("The swapped values are:", x, y)