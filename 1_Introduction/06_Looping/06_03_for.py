# Printing in the same line and not adding the "," after the last number
for i in range(1, 10):
    if i < 9:
        print("{0}, ".format(i), end="")
    else:
        print(i)
print("This is after the for")
