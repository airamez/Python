print("AUGMENTED ASSIGNMENT")
# = += -= *= /=
number = 5
print(number)

number += 1
print(number)

number += 5
print(number)

number += number
print(number)

print("ARITHMETIC OPERATIONS")
# Math class: https://docs.python.org/3.2/library/math.html
# Built-in functions: https://docs.python.org/3.1/library/functions.html
import math  # The import should be at the begin of the file

# Power
print("2^10 = ", math.pow(2, 10))

print("SQUARE ROOT")
print("25 square root = ", math.sqrt(25))

print("ABSOLUTE")
print("Absolute value of - 10 = ", math.fabs(-10))
print("Absolute value of   10 = ", math.fabs(10))

print("MAXIMUM")
print("Maximum of 3 and 7 = ", max(3, 7))
print("Maximum of 7 and 3 = ", max(7, 3))
print("Maximum of 7, 10, 3 = ", max(max(7, 10), 3))

print("MINIMUM")
print("Minimum of 3 and 7 = ", min(3, 7))
print("Minimum of 7 and 3 = ", min(7, 3))
print("Minimum of 7, 10, 3 = ", min(min(7, 10), 3))

print("PI")
print("PI = ", math.pi)

print("CEIL")
# Return the ceiling of x, the smallest integer greater than or equal to x
print("Ceil of 3.5 = ", math.ceil(3.5))
print("Ceil of -3.5 = ", math.ceil(-3.5))

print("FLOOR")
# Return the floor of x, the largest integer less than or equal to x
print("Floor of 3.5 = ", math.floor(3.5))
print("Floor of -3.5 = ", math.floor(-3.5))

print("TRUNCATE")
print("Truncate 3.99 = ", math.trunc(3.99))
print("Truncate -3.99 = ", math.trunc(-3.99))

print("ROUND")
print("Round 3.991 = ", round(3.991, 2))
print("Round 3.994 = ", round(3.994, 2))
print("Round 3.995", round(3.995, 2))
print("Round 3.996 = ", round(3.996, 2))
print("Round 3.999 = ", round(3.999, 2))

print("RANDOM NUMBERS")
import random  # The import should be at the begin of the file
# Generating a random integer number between 1 and 10 (inclusive)
randomInteger = random.randint(1, 10)
print("Random number from 1 to 10 = {0}".format(randomInteger))

print("STRING CONCATENATION")
# Concatenation: The + operator when used with string means a string concatenation operation
name = "Leila" + " " + "Rodrigues"
greetings = "Hello " + name
print(greetings)

print("Practices")
