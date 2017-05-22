print("Initializing a list with range")
months = list(range(1, 13))
print(months)

even_from_1_100 = list(range(2, 51, 2))
print(even_from_1_100)

odd_from_1_100 = list(range(1, 51, 2))
print(odd_from_1_100)

# Adding list to a list
odd_even = list()
print(odd_even)
odd_even.extend(even_from_1_100)
print(odd_even)
odd_even.extend(odd_from_1_100)
print(odd_even)
odd_even.sort()
print(odd_even)

# DANGER: Be careful when assiging values to a list because some functions doesn't return values and the list values
# will be lost
odd_even = odd_even.sort()
print(odd_even)




