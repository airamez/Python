# Declaring List
languages = list()
# languages = []

print("#1 Adding elements to a List")
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

print("#2 Print the List")
print(languages)

print("#3 List size")
print("List length =", len(languages))
print("List length =", languages.__len__())

print("#4 Accessing list elements")
for i in range(1, len(languages)):
    print(i, "=", languages[i])

print("#5 List inverted")
i = len(languages) - 1
while i >= 0:
    print(i, "=", languages[i])
    i -= 1

first = 0
print("#6 First element index = ", first)
print("First:", languages[first])

last = len(languages) - 1
print("#7 Last element index = ", last)
print("Last:", languages[last])

print("#8 Count")
pythonCount = languages.count("Python")
print("Python Count =", pythonCount)

print("#9 Changing elements")
print(languages)
languages[9] = "PHP"
print(languages)

print("#10 Removing an element at a specific index")
removed = languages.pop(3)
print("Removed element at index 3 =", removed)
print(languages)

print("#11 Removing the last element")
removed = languages.pop()
print("Removed element =", removed)
print(languages)

print("#12 Removing the first occurrence of a element based on the value")
languages.remove("Python")
print("First Python removed")
print(languages)

print("#13 Remove raise an Error if the element doesn't not exist")
try:
    languages.remove("Ruby")
except ValueError as e:
    print(e)

print("#14 Inserting an element at a specific index")
languages.insert(0, "Delphi")
languages.insert(4, "Lua")
languages.insert(len(languages), "Python")  # Insert at last index == Append
print(languages)

print("#15 Finding the first index of an element")
first_python = languages.index("Python")
print("First Python =", first_python)

print("#16 Index raise an Error if doesn't find")
try:
    first_cobol = languages.index("Cobol")
except ValueError as e:
    print(e)

print("#17 Checking if exists")
if "Python" in languages:
    print("Python found")
print("PythonXX" in languages)

print("#18 Checking if NOT exists")
if "Cobol" not in languages:
    print("Cobol NOT found")

print("#19 Reversing the entire list")
print(languages)
languages.reverse()
print(languages)

print("#20 Sorting the list")
languages.sort()
print(languages)

print("#21 Slice")
'''
a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
'''
languages_2_to_4_end = languages[2:5]
print("[2:5]", languages_2_to_4_end)
languages_5_to_end = languages[5:]
print("[5:]", languages_5_to_end)
languages_0_to_5 = languages[:6]
print("[:6]", languages_0_to_5)
languages_copy = languages[:]
print("[:]", languages_copy)
print("List =", languages)

print("#22 Cleaning the list")
languages.clear()
print(languages)

print("Initializing a list with range")
months = list(range(1, 13))
print(months)

even_from_1_100 = list(range(2, 101, 2))
print(even_from_1_100)
