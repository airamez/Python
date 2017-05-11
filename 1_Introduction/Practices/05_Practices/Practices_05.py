"""
Read two integer numbers and print them in ascending order
"""

number_1 = int(input("Number 1 = "))
number_2 = int(input("Number 2 = "))

# Option 1
if number_1 < number_2:
    print(number_1, number_2)
else:
    print(number_2, number_1)

# Option 2
if number_1 <= number_2:
    print(number_1, number_2)
else:
    print(number_2, number_1)

# Option 3
if number_1 > number_2:
    print(number_2, number_1)
else:
    print(number_1, number_2)

# Option 4
if number_1 >= number_2:
    print(number_2, number_1)
else:
    print(number_1, number_2)

# Option 5
if number_2 < number_1:
    print(number_2, number_1)
else:
    print(number_1, number_2)

# Option 6 : if inline
output = "{0} {1}".format(number_1, number_2) if number_1 < number_2 else "{0} {1}".format(number_2, number_1)
print(output)
