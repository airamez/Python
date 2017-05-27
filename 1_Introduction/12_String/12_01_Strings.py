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

print("# Is Alpha (Alphabetic)")
print("abcd".isalpha())
print("abcd.".isalpha())
print("abcd123".isalpha())
print("".isalpha())

print("# Is Numeric")
print("123456789".isnumeric())
print("12334abc".isnumeric())
print("".isnumeric())

print("# Is Space")
print(" ".isspace())
print("       ".isspace())
print("  coding    ".isspace())
print("".isspace())

