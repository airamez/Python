"""
Read three integer numbers and print them in ascending order
"""

n1 = int(input("Number 1 = "))
n2 = int(input("Number 2 = "))
n3 = int(input("Number 3 = "))

# Option 1
if n1 <= n2 <= n3:
    print(n1, n2, n3)
elif n1 <= n3 <= n2:
    print(n1, n3, n2)
elif n2 <= n1 <= n3:
    print(n2, n1, n3)
elif n2 <= n3 <= n1:
    print(n2, n3, n1)
elif n3 <= n1 <= n2:
    print(n3, n1, n2)
else:
    print(n3, n2, n1)

# Option 2
if n1 > n2:  # Making sure n1 and n2 get in order
    n1, n2 = n2, n1
# Finding where n3 should be
if n3 <= n1:
    print(n3, n1, n2)
elif n3 <= n2:
    print(n1, n3, n2)
else:
    print(n1, n2, n3)
