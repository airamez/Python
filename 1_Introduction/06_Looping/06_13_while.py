"""
Game to find a number from 0 to 9
"""

import random

rnd = random.randint(0, 9)

count = 0
# "do while" simulation
while True:
    guess = int(input("Type a number between 0 and 9 = "))
    count += 1
    if guess == rnd:
        print("Congratulations! You found the number with {0} attempts".format(count))
        break
