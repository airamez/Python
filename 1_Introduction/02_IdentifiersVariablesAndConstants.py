'''
IDENTIFIERS
An identifier is a name used to identify something in a program.
In Python an identifier is case sensitive, and starts with a letter, or
an underscore (_) followed by zero or more letters, underscores or digits (0 to 9)
PS: An identifier can't start with a number (This is valid for all languages I know)

RESERVED WORDS:
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try

VARIABLES and CONSTANTS
A variable in Python doesn't need a type and the assigned value will define the variable type
'''

# Integer
age = 44  # Declaring and assigning an integer value
print(age)

# Floating point
payment = 345.67
print(payment)

# Boolean
approved = True
print(approved)
approved = False
print(approved)

# String variables
name = "José Santos"  # A string constant is define by " or '
name = 'José Santos'
print(name)

course = 'Learning Python'
print(course)

# Multiple lines string constant
essay = '''Family
José Santos
Leila Rodrigues
Artur Rodrigues'''
print(essay)

# Escape characters
content = "Content\n\t - Item 1\n\t - Item 2\n\t\t - Item 2.1\n\t - Item 3"
print(content)

line = "This string has the \\, the \' and the \" characters"
print(line)

# Assigning different types to the same identifier
variable = 5
print(type(variable))

variable = 5.5
print(type(variable))

variable = True
print(type(variable))

variable = 'We love coding'
print(type(variable))
