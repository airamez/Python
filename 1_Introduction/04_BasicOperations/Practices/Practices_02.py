import random

"""
Read two integer numbers in natural order and generate a random number between them.
e.g.
 INPUT
   Number1 = 23
   Number2 = 45
 OUTPUT
   Random Number = 37
"""

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

rnd = random.randint(number1, number2)

print("The random number is", rnd)
