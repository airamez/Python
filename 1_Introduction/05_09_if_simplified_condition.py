"""
Generate a integer interval from 0 and 100 and let the user try a number, after the try inform if the
number is inside or outside of the interval
"""
import random

left = random.randint(0, 50)
right = random.randint(left + 1, 100)
number = int(input("Type a number between 0 and 100 = "))
print("Interval [{0}..{1}]".format(left, right))

# Method 1
if left <= number and number <= right:
    print("Number inside the the interval!")
else:
    print("Number is outside the interval!")

# Method 2: Simplified
if left <= number <= right:
    print("Number inside the the interval!")
else:
    print("Number is outside the interval!")

# Method 3: Inverted logical conditions
if number < left or number > right:
    print("Number is outside the interval!")
else:
    print("Number inside the the interval!")
