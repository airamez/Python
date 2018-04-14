start = 0
end = 10

# Nested loops
# Prints the multiplication table
for i in range(start, end + 1):
    for j in range(start, end + 1):
        print("{0} x {1} = {2}".format(i, j, i * j))
print("This is a command after the for loops")
