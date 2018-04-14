"""
Game to find a number from 0 to 9
"""

import random

rnd = random.randint(0, 9)

count = 1

guess = int(input("Type a number between 0 and 9 = "))
while guess != rnd:
    guess = int(input("Type a number between 0 and 9 = "))
    count += 1

print("Congratulations! You found the number with {0} attempts".format(count))

