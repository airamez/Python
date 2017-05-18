import random

MIN = 0
MAX = 99
numbers = (random.randint(MIN, MAX), random.randint(MIN, MAX), random.randint(MIN, MAX), random.randint(MIN, MAX),
           random.randint(MIN, MAX), random.randint(MIN, MAX), random.randint(MIN, MAX), random.randint(MIN, MAX))
print(numbers)
print("MAX =", max(numbers))
print("MIN =", min(numbers))

# Create a list from a tuple
numbers_list = list(numbers)

numbers_list[0] = 1
numbers_list[1] = 2
numbers_list[len(numbers_list) - 1] = 9

print(numbers_list)
print(numbers)

# Creating a tuple from a list
numbers_tuple = tuple(numbers_list)
print(numbers_tuple)
