"""
The if command provide the capability to control the flow of a program by checking conditions and 
executing or not parts of the program.
Comparisons operator:
==  Equal
!=  Not Equal
<   Smaller than
>   Greater than
>=  Greater or Equal than
<=  Smaller or Equal than
"""

age = int(input('Type your age: '))

if age >= 18:
    print('----------------')
    print("You are an adult. Age =", age)
    print('----------------')
    # Everything align inside the if statement is part of the if statement
    # Python uses indentation to define statement blocks. Many others languages use open and close delimiters
    # like { and }
print("This is outside the if statement and it will be always executed")
