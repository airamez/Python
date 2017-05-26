# Declaring a dictionary
months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
          7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
print("Months =", months)

# Getting the keys
print(months.keys())

# Getting the Values
print(months.values())

# Accessing an value from a key as an index
print("months[3] =", months[3])
print("months[5] =", months[5])
print("months[11] =", months[11])
# Accessing a key that doesn't exist raise an exception
try:
    print(months[99])  # Raise an exception
except KeyError as e:
    print(type(e), e)

# Accessing a value from a key using the get method
print("months.get(3) =", months.get(3))
# Accessing a key that doesn't exist
print("months.get(99) =", months.get(99))  # Doesn't raise exception
# Accessing a value from a key using the get method and using a default value
print('months.get(99, "N/A") =', months.get(99, "N/A"))

# Deleting an Key/Value
print("Months =", months)
del months[5]
print("Months =", months)
try:
    del months[5]  # Raise an exception
except KeyError as e:
    print(type(e), e)

# Replacing a Value
months[5] = "Maio"
print("Months =", months)
months[5] = "May"
print("Months =", months)

# Removing elements
may = months.pop(5)
print(may)
print("Months =", months)
try:
    may = months.pop(5)  # Raise an exception
except KeyError as e:
    print(type(e), e)
# Removing using a Default value
may = months.pop(5, "N/A")
print(may)
may = months.pop(5, None)
print(may)

countries = dict()
countries["BRA"] = "Brazil"
countries["CAN"] = "Canada"
countries["USA"] = "United States of America"
countries["MEX"] = "Mexico"
print("Countries =", countries)
print("BRA = ", countries["BRA"])
if "CAN" in countries:
    print(countries["CAN"])
if "BR" not in countries:
    print("BR not found")

# Cleaning a dict
countries.clear()
print("Countries =", countries)
