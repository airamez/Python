"""
Read two integer numbers storing each one in a variable and switch the variable values.
"""

# Method 1
number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))

aux = number1
number1 = number2
number2 = aux

print("Number 1 = ", number1)
print("Number 2 = ", number2)

# Method 2
number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))

number1, number2 = number2, number1

print("Number 1 = ", number1)
print("Number 2 = ", number2)


