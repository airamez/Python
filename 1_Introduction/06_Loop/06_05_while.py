start = 1
end = 10

# Prints the number from start to end in the same line
i = start
while i <= end:
    print("{0}, ".format(i), end="")
    i += 1
    # Everything aligned/indented inside the while statement is part of the while statement
print()