"""
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
"""

# Integer
age = 44  # Declaring and assigning an integer value
print(age)  # Prints to the default output

# Floating point
payment = 345.67
print(payment)

# Boolean
approved = True
print(approved)
approved = False
print(approved)

# String variables
name = "José Santos"  # A string constant is define by ', ", ''' or """
print(name)
name = 'José Santos'
print(name)
name = """José Santos"""
print(name)

course = 'Learning Python'
print(course)

# Multiple lines string constant
family = '''Family:
'José' "Santos"
'Leila' "Rodrigues"
'Artur' "Rodrigues"'''
print(family)

family = """Family:
"José" 'Santos'
"Leila" 'Rodrigues'
"Artur" 'Rodrigues'"""
print(family)

family = "Family: " \
        "José Santos; " \
        "Leila Rodrigues; " \
        "Artur Rodrigues"
print(family)


# Escape characters:
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

# Interesting concept
a = 1
b = a
print(a, b)
b = 2
print(a, b)

a = "Leila"
b = a
print(a, b)
b = "Artur"
print(a, b)
