phrase = "I Love Computer Programming"

print("# Split")
words = phrase.split()
print(phrase)
print(words)

phrase = "I;Love;Computer;Programming"
words = phrase.split(";")
print(phrase)
print(words)

phrase = "I<->Love<->Computer<->Programming"
words = phrase.split("<->")
print(phrase)
print(words)

print("# Partition")
phrase = "I really love computer programming so much"
print(phrase)
phrase_partition = phrase.partition("computer")
print(phrase_partition)

print("#Split Lines")
paragraph = """Line 1
Line 2
Line 3
Line 4
Line 5
"""
lines = paragraph.splitlines()
print(lines)
