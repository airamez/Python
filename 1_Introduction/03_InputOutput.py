'''
Class notes: Input/Output (I/O)
 * Most of programs need to acquire or provide data/information
 * The source and target of the I/O operations can be a person (User) or a device (printer, mouse, keyboard, etc)
 * There are input, output and input/output devices
 * Graphical User Interface is the most common way to interact with users
 * The three mainstypes of user I/O
   * Console
   * Windows
   * Web
   * Could we find others?
'''

name = input("Type your name: ")  # The input command always returns a string
# The + operator can be used to concatenate strings
print("Hello " + name + ", welcome to the Learning Python course")

age = input("What is your age: ")
print(age)

print("Type two numbers and I will calculate the average")
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
average = (number1 + number2) / 2
print("The average of the numbers", number1, "and", number2, "is", average)

payment = float(input("Payment value: "))  # Converting the input to float
print(payment)

# Printing 3 variables
print(name, age, payment)

# Printing with descriptions
print("Name =", name, "; Age =", age, "; Payment =", payment)

# Printing using format (parameters by order)
message = "Name = {0}; Age = {1}; Payment = {2}".format(name, age, payment)
print(message)

# Printing using format (parameters by name)
message = "Name = {name}; Age = {age}; Payment = {payment}".format(payment=payment, age=age, name=name)
print(message)

# If we want to print without move to a new line
print('1', end='')
print('2', end='')
print('3', end='')
print('4', end='')
print('5', end='')

# Every variable has a type

myInteger = 5  # Integer

myFloat = 10.5  # Float

myString = "I love coding"  # String

myInteger = int("145")  # Integer from string
print(myInteger)

# Show the error
# myInteger = int("145.67")
print(myInteger)

myFloat = float("145")
print(myFloat)

myFloat = float("145.67")
print(myFloat)

# myFloat = float("ABC 145.67")
print(myFloat)

myString = str(10)
print(myString)

myString = str(145.67)
print(myString)

# One variable could received different types
myVariable = 10
print(myVariable)

myVariable = 10.45
print(myVariable)

myVariable = "I am a string"
print(myVariable)

myVariable = True
print(myVariable)

print("Practices")

