"""
Read four numbers and calculate the weighted average using the weights 2, 2, 2, 4.
"""
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

weightedAverage = ((n1 * 2) + (n2 * 2) + (n3 * 2) + (n4 * 4)) / 10

print(weightedAverage)
