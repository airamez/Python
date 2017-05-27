"""
Read two integer numbers A and B and inform if A is divisible by B and if it is not divisible
print the remainder.
"""

number_a = int(input("Number A = "))
number_b = int(input("Number B = "))

# Option 1
if number_a % number_b == 0:
    print("{0} is divisible by {1}".format(number_a, number_b))
else:
    print("{0} is NOT divisible by {1} and the remainder is {2}".format(number_a, number_b, number_a % number_b))

# Option 2
remainder = number_a % number_b
if remainder == 0:
    print("{0} is divisible by {1}".format(number_a, number_b))
else:
    print("{0} is NOT divisible by {1} and the remainder is {2}".format(number_a, number_b, remainder))

# Option 3
if remainder != 0:
    print("{0} is NOT divisible by {1} and the remainder is {2}".format(number_a, number_b, remainder))
else:
    print("{0} is divisible by {1}".format(number_a, number_b))
