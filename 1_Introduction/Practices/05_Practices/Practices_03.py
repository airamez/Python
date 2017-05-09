"""
Read a number and inform if the number is positive, negative or zero.
"""

number = float(input("Number = "))

# Option 1
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")

# Option 2
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Option 3
if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("Positive")
