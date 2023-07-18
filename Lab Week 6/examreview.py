#Akhil Pallem 9-26-22
#Lab week 6 
#Exam Review section 
print("Question 1")
a = 2
b = 3
c = 0
c = a % b
print("c = a % b | H: {0} C: {1}".format("2", c))
c *= 2
print("c *= 2 | H: {0} C: {1}".format("4", c))
c += a ** b
print("c += a ** b | H: {0} C: {1}".format("12", c))
c //= b * (a + a)
print("c //= b * (a + a) | H: {0} C: {1}".format("1", c))
c += c
print("c += c | H: {0} C: {1}".format("2", c))
c += c
print("c += c | H: {0} C: {1}".format("4", c))
c += c
print("c += c | H: {0} C: {1}".format("8", c))
c -= c * b
print("c -= c * b | H: {0} C: {1}".format("-16", c))
print()


print("Question 2")
a = 4
b = 4
c = a ** b - 1
print("c = a ** b - 1 | H: {0} C: {1}".format("255", c))
c -= b ** a % b
print("c -= b ** a % b | H: {0} C: {1}".format("255", c))
c %= a
print("c %= a | H: {0} C: {1}".format("3", c))
b = c
c += b
print("c += b | H: {0} C: {1}".format("6", c))
a = c + b
c -= c + a
print("c -= c + a | H: {0} C: {1}".format("-9", c))
c *= c
print("c *= c | H: {0} C: {1}".format("81", c))
c -= c
print("c -= c | H: {0} C: {1}".format("0", c))
c += c + a + b
print("c += c + a + b | H: {0} C: {1}".format("12", c))
print()

print("Question 3")
a = 3
b = 2
c = a * b + 1
print("c = a * b + 1 | H: {0} C: {1}".format("7", c))
b += a
c -= b % a % b
print("c -= b % a % b | H: {0} C: {1}".format("5", c))
c += a
print("c += a | H: {0} C: {1}".format("8", c))
b = c + a
a = c + b
c *= b
print("c *= b | H: {0} C: {1}".format("88", c))
a = c - b
c += c + a
print("c += c + a | H: {0} C: {1}".format("253", c))
c %= c
print("c %= c | H: {0} C: {1}".format("0", c))
c -= c + 1
print("c -= c + 1 | H: {0} C: {1}".format("-1", c))
c += c + 1 + b
print("c += c + 1 + b | H: {0} C: {1}".format("10", c))
print()


print("Question 4")
a = True
b = True
c = a and b
print("c = a and b | H: {0} C: {1}".format("True", c))
a = True
b = True
c = a and not b
print("c = a and not b | H: {0} C: {1}".format("False", c))
a = True
b = False
c = not (a and not b)
print("c = not (a and not b) | H: {0} C: {1}".format("False", c))
a = True
b = False
c = not (a and not b) or not (not a or b)
print("c = not (a and not b) or not (not a or b) | H: {0} C: {1}".format("True", c))
a = False
b = True
c = not (not (a and not b) or not (not a or b))
print("c = not (not (a and not b) or not (not a or b)) | H: {0} C: {1}".format("False", c))
print()


print("Question 5")
a = True
b = True
c = True
d = a and b and not c
print("d = a and b and not c | H: {0} C: {1}".format("False", d))
a = True
b = False
c = True
d = not (a and b and not (not c or a))
print("d = not (a and b and not (not c or a)) | H: {0} C: {1}".format("True", d))
a = True
b = False
c = False
d = not a or not (not a or b and not (not c and a))
print("d = not a or not (not a or b and not (not c and a)) | H: {0} C: {1}".format("True", d))
a = False
b = False
c = True
d = not b or c and not (not a or not (not a or b or not (not c or a)))
print("d = not b or c and not (not a or not (not a or b or not (not c or a))) | H: {0} C: {1}".format("True", d))
print()