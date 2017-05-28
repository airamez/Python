"""
String in Python is an immutable collection of Unicode characters
UNICODE: https://en.wikipedia.org/wiki/Unicode
         https://unicode-table.com/en/#control-character
"""

print('ord("A") =', ord("A"), hex(ord("A")))
print("chr(65) =", chr(65))

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvxwyz0123456789"
print(s)
for i in range(0, len(s)):
    print("Char = {}; Code = {} {}".format(s[i], ord(s[i]), hex(ord(s[i]))))

CHARS_PER_LINE = 16
for i in range(0, 2 ** 16, CHARS_PER_LINE):
    for j in range(i, i + CHARS_PER_LINE):
        try:
            char = chr(j)
            print("[{}={}]".format(hex(ord(char)), char), end='')
        except UnicodeEncodeError:
            pass
    print()



