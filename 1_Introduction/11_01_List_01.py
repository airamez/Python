# Declaring List
languages = list()
# languages = []

print("# Adding elements to a List")
languages.append("Python")
languages.append("Java")
languages.append("C#")
languages.append("Python")
languages.append("JavaScript")
languages.append("Python")
languages.append("SQL")
languages.append("C")
languages.append("C++")
languages.append("COBOL")

print("# Print the List")
print(languages)

print("# List size")
print("List length =", len(languages))
print("List length =", languages.__len__())

print("# Accessing list elements")
for i in range(1, len(languages)):
    print(i, "=", languages[i])

print("# List inverted")
i = len(languages) - 1
while i >= 0:
    print(i, "=", languages[i])
    i -= 1

first = 0
print("# First element index = ", first)
print("First:", languages[first])

last = len(languages) - 1
print("# Last element index = ", last)
print("Last:", languages[last])

print("# Count")
pythonCount = languages.count("Python")
print("Python Count =", pythonCount)

print("Changing elements")
print(languages)
languages[9] = "PHP"
print(languages)

print("# Removing an element at a specific index")
removed = languages.pop(3)
print("Removed element at index 3 =", removed)
print(languages)

print("# Removing the last element")
removed = languages.pop()
print("Removed element =", removed)
print(languages)

print("# Removing the first occurrence of a element based on the value")
languages.remove("Python")
print("First Python removed")
print(languages)

print("# Inserting an element at a specific index")
languages.insert(0, "Delphi")
languages.insert(4, "Lua")
languages.insert(len(languages), "Python")  # Insert at last index == Append
print(languages)

print("# Finding the first index of an element")
first_python = languages.index("Python")
print("First Python =", first_python)

print("# Finding the last index of an element")

print("# Reversing the entire list")
print(languages)
languages.reverse()
print(languages)

print("# Sorting the list")
languages.sort()
print(languages)

print("# Cleaning the list")
languages.clear()
print(languages)
