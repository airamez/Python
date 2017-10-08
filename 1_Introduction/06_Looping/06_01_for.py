# for using range [start, end[
for i in range(1, 10):
    print(i)
    # All commands aligned inside the for it part of the for looping

# for printing in the same line
for i in range(1, 10):
    print("{0}, ".format(i), end="")

print()

# Printing in the same line and not adding the "," after the last number
for i in range(1, 10):
    if i < 9:
        print("{0}, ".format(i), end="")
    else:
        print(i)
print("This is a command after the for loop")
