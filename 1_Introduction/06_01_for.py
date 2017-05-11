# for using range [start, end[
for i in range(1, 10):
    print(i, end='')
    print(', ', end='')
    # All command aligned inside the for it part of the for looping

start = 1
end = 10
for i in range(start, end + 1):
    print('{0}{1} '.format(i, "," if i != end else ""), end="")
print()

for i in range(0, 100, 5):
    print('{0}{1} '.format(i, "," if i != end else ""), end="")
print()

# Nested loops
# Prints the multiplication table
for i in range(start - 1, end + 1):
    for j in range(start - 1, end + 1):
        print("{0} x {1} = {2}".format(i, j, i * j))
