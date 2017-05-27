phrase = "I Love Computer Programming"

print("Substring/Slicing")
print(phrase[0: 1])
print(phrase[2: 6])
print(phrase[7:15])
print(phrase[7:])
print(phrase[:15])

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

print("# Capitalize")
phrase_capitalized = phrase_lower.capitalize()
print(phrase_capitalized)

print("# Title")
phrase_titled = phrase_upper.title()
print(phrase_titled)

print("# Test Title")
print(phrase_titled.istitle())
print(phrase_lower.istitle())
print(phrase_upper.istitle())

print("# Swap case")
print(phrase_lower, "=>", phrase_lower.swapcase())
print(phrase_upper, "=>", phrase_upper.swapcase())
print(phrase_titled, "=>", phrase_titled.swapcase())

print("# Strip")
not_stripped = "    coding               "
print('"{}"'.format(not_stripped))
stripped = not_stripped.strip()
print(stripped)

not_stripped = "XXXXXXcodingXXX"
print('"{}"'.format(not_stripped))
stripped = not_stripped.strip("X")
print(stripped)

not_stripped = "XYZXYZcodingXYZXYZ"
print('"{}"'.format(not_stripped))
stripped = not_stripped.strip("XYZ")
print(stripped)

print("# Left/Right Strip")
not_stripped = "    coding               "
stripped = not_stripped.lstrip()
print("Left Stripped = [{}]".format(stripped))
stripped = not_stripped.rstrip()
print("Right Stripped = [{}]".format(stripped))

print("# Center")
base = "center"
centralized = base.center(50, "_")
print(centralized)

print("# Left Justify")
left_justified = base.ljust(30, "_")
print(left_justified)

print("# Right Justify")
right_justified = base.rjust(30, "_")
print(right_justified)

print("# Replace")
print(phrase)
new_phrase = phrase.replace("Love", "Enjoy")
print(new_phrase)
new_phrase = phrase.replace("m", "")
print(new_phrase)

print("# ZFill")
s = "7.45"
print(s.zfill(10))
s = "+7.45"
print(s.zfill(10))
s = "-7.45"
print(s.zfill(10))
