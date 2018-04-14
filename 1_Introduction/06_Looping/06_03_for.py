# Printing in the same line and not adding the "," after the last number

# 1
for i in range(1, 10):
    if i < 9:
        print("{0}, ".format(i), end="")
    else:
        print(i)
print("This is after the for")

# 2
for i in range(1, 10):
    print("{0}{1}".format(i, ", " if i < 9 else "\n"), end="")
print("This is after the for")
