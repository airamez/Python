age = int(input('Type your age: '))

# if
if age >= 18:
    print('----------------')
    print("You are an adult. Age =", age)
    print('----------------')
    # Everything align inside the if statement is part of the if statement
    # Python uses indentation to define statement blocks. Many others languages use open and close delimiters
    # like { and }

print("This is outside the if statement and it will be always executed")
