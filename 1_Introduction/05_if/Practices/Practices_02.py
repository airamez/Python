"""
Read two integer numbers and inform if the numbers are equals or different.
"""
number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))

# Option 1
if number1 == number2:
    print("Equals")
else:
    print("Different")

# Option 2
if number1 != number2:
    print("Different")
else:
    print("Equals")

# Option 3
if not number1 != number2:
    print("Equals")
else:
    print("Different")

# Option 4
if not number1 == number2:
    print("Different")
else:
    print("Equals")
