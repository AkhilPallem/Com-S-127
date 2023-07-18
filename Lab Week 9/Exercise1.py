import random
#Akhil Pallem lab week 9 

def function(a, b):
    list = []
    list2 = []
    for i in range (a):
        numbers = random.randint(a, a+b)
        list.append(numbers)
    for number in list:
        if number % b == 0:
            list2.append(number)
    print(list)
    return list2


a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
print(function(a, b))