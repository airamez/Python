"""
Read four numbers and print the numbers with the smallest value and largest value
"""
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

minimum = min(min(min(n1, n2), n3), n4)
maximum = max(max(max(n1, n2), n3), n4)

print("Minimum", minimum)
print("Maximum", maximum)

