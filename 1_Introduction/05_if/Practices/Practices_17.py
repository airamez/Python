"""
Read four integer numbers and print the ones divisible by 2 and 3.
"""

number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))
number3 = int(input("Number 3 = "))
number4 = int(input("Number 4 = "))

if number1 % 2 == 0 and number1 % 3 == 0:
    print(number1)

if number2 % 2 == 0 and number2 % 3 == 0:
    print(number2)

if number3 % 2 == 0 and number3 % 3 == 0:
    print(number3)

if number4 % 2 == 0 and number4 % 3 == 0:
    print(number4)
