"""
Read two integer numbers storing them into two Variables Number1 and Number2 and make sure that
Number1 and Number2 variables get in ascending order.
"""
Number1 = int(input("Number 1 = "))
Number2 = int(input("Number 2 = "))

# Option 1
"""
if Number2 < Number1:
    aux = Number1
    Number1 = Number2
    Number2 = aux
"""

# Option 2
"""
if Number1 > Number2:
    aux = Number1
    Number1 = Number2
    Number2 = aux
"""

# Option 3
if Number1 > Number2:
    Number1, Number2 = Number2, Number1

print(Number1, Number2)
