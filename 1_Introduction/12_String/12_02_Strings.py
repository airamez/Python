phrase = "I Love Computer Programming"

print("# In and Not In")
print("Love" in phrase)
print("Love" not in phrase)
print("Python" in phrase)
print("Python" not in phrase)

print("# Find")
print(phrase)
print(phrase.find("Programming"))
print(phrase.find("Coding"))
print(phrase.find("m", 0))
print(phrase.find("m", 10))
print(phrase.find("Love", 0, 10))
print(phrase.find("Love", 20, 25))

print("# Right Find")
print(phrase.rfind("m"))
print(phrase.rfind("ming"))
print(phrase.rfind("m", 0, 10))
print(phrase.rfind("Python"))

print("# Starts with")
print(phrase)
print(phrase.startswith("I"))
print(phrase.startswith("B"))
print(phrase.startswith("I Love"))
print(phrase.startswith("Love"))

print("# Ends with")
print(phrase)
print(phrase.endswith("g"))
print(phrase.endswith("k"))
print(phrase.endswith("Programming"))
print(phrase.endswith("Computer"))

print("# Count")
s = "aaabbb aaabbb"
print(s.count("a"))
print(s.count("b"))
print(s.count("c"))
print(s.count("aaa"))
print(s.count("aaabbb"))

