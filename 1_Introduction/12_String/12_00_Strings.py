"""
String in Python is an immutable collection of Unicode characters
UNICODE: https://en.wikipedia.org/wiki/Unicode
         https://unicode-table.com/en/#control-character
"""
s = "abcdefghijklmnopqrstzywz"
s = "0123456789" + s.upper() + s
print(s)
for i in range(0, len(s)):
    print("Char = {}; Code = {}".format(s[i], ord(s[i])))

CHARS_PER_LINE = 100
for i in range(0, 2 ** 16, CHARS_PER_LINE):
    for j in range(i, i + CHARS_PER_LINE):
        try:
            char = chr(j)
            if char.isprintable():
                print(char, end='')
        except UnicodeEncodeError:
            pass
    print()



