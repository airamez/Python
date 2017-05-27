"""
String in Python is an immutable collection of Unicode characters
UNICODE: https://en.wikipedia.org/wiki/Unicode
"""

phrase = "I Love Computer Programming"

print("# Accessing a character at a specific index")
first_character = phrase[0]
last_character = phrase[len(phrase) - 1]
print("First = {}; Last = {}".format(first_character, last_character))
# An exception is raised if an invalid index is accessed
try:
    print(phrase[100])
except IndexError as e:
    print(e)

print("# String concatenation")
first_name = "José"
last_name = "Santos"
full_name = first_name + " " + last_name
print("Full Name =", full_name)
# The concatenation requires all types to be converted to string
integer = 10
try:
    new_string = phrase + integer
except TypeError as e:
    print(e)
new_string = phrase + str(integer)
print(new_string)

print("# Accessing all characters of a string")
for c in first_name:
    print(c)
for i in range(0, len(first_name)):
    print("first_name[{}] = {}".format(i, first_name[i]))

print("# Lower/Upper Case")
phrase_lower = phrase.lower()
print(phrase_lower)
phrase_upper = phrase.upper()
print(phrase_upper)

print("# Testing Lower/Upper Case")
print(phrase_lower.islower())
print(phrase_lower.isupper())
print(phrase_upper.islower())
print(phrase_upper.isupper())

print("# Strip")
not_stripped = "    coding               "
stripped = not_stripped.strip()
print(stripped)

not_stripped = "XXXXXXcodingXXX"
stripped = not_stripped.strip("X")
print(stripped)

not_stripped = "XYZXYZcodingXYZXYZ"
stripped = not_stripped.strip("XYZ")
print(stripped)

print("# Left/Right Strip")
not_stripped = "    coding               "
stripped = not_stripped.lstrip()
print("Left Stripped = [{}]".format(stripped))
stripped = not_stripped.rstrip()
print("Right Stripped = [{}]".format(stripped))

print("# Is Alpha (Alphabetic)")
print("abcd".isalpha())
print("abcd.".isalpha())
print("abcd123".isalpha())
print("".isalpha())

print("# Is Digit (Numbers)")
print("123456789".isdigit())
print("12334abc".isdigit())
print("700.45".isdigit())
print("".isdigit())

print("# Is Space")
print(" ".isspace())
print("       ".isspace())
print("  coding    ".isspace())
print("".isspace())

print("# Find")
print(phrase)
print(phrase.find("Programming"))
print(phrase.find("Coding"))
print(phrase.find("m", 0))
print(phrase.find("m", 10))
print(phrase.find("Love", 0, 10))
print(phrase.find("Love", 20, 25))

