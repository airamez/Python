"""
Read an integer number and inform if the number is odd or even
"""
ODD = "Odd"
EVEN = "Even"
number = int(input("Number = "))

# Option 1
if number % 2 == 1:
    print(ODD)
else:
    print(EVEN)

# Option 2
if number % 2 == 0:
    print(EVEN)
else:
    print(ODD)

# Option 3
print(EVEN if number % 2 == 0 else ODD)

# Option 4
if number % 2 != 1:
    print(EVEN)
else:
    print(ODD)

# Option 5
if number % 2 != 0:
    print(ODD)
else:
    print(EVEN)
