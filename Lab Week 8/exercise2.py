#Akhil Pallem 
#10-10-22 
#Lab Week 8 

def tuple(x, y, z):
    if x > y and x > z and y > z:
        return (x, y, z)
    elif y > x and y > z and x > z:
        return (y, x, z)
    elif z > y and z > x and y > z: 
        return (z, y, x)
    elif z > y and z > x and x > y: 
        return (z, x, y)
    elif x > y and x > z and z > y:
        return (x, z, y)
    elif y > x and y > z and z > x:
        return (y, z, x)
    elif z > y and z > x and y > x:
        return(z, y, x)

a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
c = int(input("Enter an integer: "))
final = tuple(a, b, c)
print("The values sorted are: " + str(final))
