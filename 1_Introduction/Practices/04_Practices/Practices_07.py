import math

"""
Read the two sides of a triangle and calculate the hypotenuse.
h2 = a2 + b2
"""
a = int(input("Side A: "))
b = int(input("Side B: "))

h = math.sqrt((math.pow(a, 2) + math.pow(b, 2)))

print("Hypotenuse = ", h)

