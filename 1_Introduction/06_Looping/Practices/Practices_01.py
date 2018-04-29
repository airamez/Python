"""
01. Print the numbers from 1 to 1000 without using new lines after each number.
"""
for number in range(1, 1001):
    print(str(number) + ' ', end='')

print()

for number in range(1, 1001):
    print("{0} ".format(number), end='')

