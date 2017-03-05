print("ASSIGNMENT")
number1 = 10
number2 = 7
print("number1 = {0}; number2 = {1}".format(number1, number2))

# Multiple variable assignment in a single line. Attention: Better to avoid this :P
myInteger, myFloat, s = 10, 10.5, "Learning Python"
print(myInteger, myFloat, s)

# One value to multiple variables
a = b = c = d = e = 15
print(a, b, c, d, e)

print("ADDITION")
number3 = number1 + number2 + 2
print("{0} + {1} + 2 = {2}".format(number1, number2, number3))
number1 = number1 + 3
print("number1 = {0}".format(number1))

print("SUBTRACTION")
number4 = number1 - number3
print("{0} - {1} = {2}".format(number1, number3, number4))

print("NEGATIVE")
number = 10
print(number)
number = -number
print(number)

print("MULTIPLICATION")
number5 = number1 * number2 * 2
print("{0} x {1} x 2 = {2}".format(number1, number2, number5))

print("DIVISION")
myFloat = 7 / 2
print("7 / 2 = {0}".format(myFloat))

print("INTEGER DIVISION")
print("7 / 2 =", 7 // 2)
print("11 / 2 =", 11 // 2)
print("10 / 2 =", 10 // 2)
print("3 / 7 =", 3 // 7)

print("REMAINDER/MOD")
print("7 % 2 =", 7 % 2)
print("3 % 2 =", 3 % 2)
print("4 % 2 =", 4 % 2)
print("3 % 7 =", 3 % 7)

print("DIV/MOD")
division = divmod(7, 2)
print("7 / 2", "Div=", division[0], "Mod=", division[1])

print("power")
print("2**10 = ", 2**10)

print("OPERATION PRIORITY")
average = (number1 + number2 + number3) / 3
print("The average of {0}, {1} and {2} is {3}".format(number1, number2, number3, average))
