"""
Generate an random integer number with 4 digits and generate another number with the digits in reverse order.
    e.g.
    Number = 1234
    Inverted = 4321
"""
import random
number = random.randint(1000, 9999)

number_copy = number

division = divmod(number, 10)
inverted = division[1]
number = division[0]

division = divmod(number, 10)
inverted = inverted * 10 + division[1]
number = division[0]

division = divmod(number, 10)
inverted = inverted * 10 + division[1]
number = division[0]

division = divmod(number, 10)
inverted = inverted * 10 + division[1]

print(number_copy)
print(inverted)
