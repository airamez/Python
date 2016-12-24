# while
start = 1
end = 10
i = start
while i <= end:
    print("{0}, ".format(i), end="")
    i += 1
    # Everything aligned/indented inside the while statement is part of the while statement

print()

# Removing the last ','
i = start
while i <= end:
    if i < end:
        print("{0}, ".format(i), end="")
    else:
        print(i)
    i += 1

# while, continue and break
i = start
while True:
    i += 1
    if i % 2 != 0:
        continue  # Jump tp the begin of the while ignore the next statements
    if i >= 10:
        break  # Ends the loop
    print("{0}, ".format(i), end="")

print()

# for using range [start, end[
for i in range(1, 10):
    print('{0}, '.format(i), end="")

print()
for i in range(start, end + 1):
    print('{0}{1} '.format(i, "," if i != end else ""), end="")

# nested loops
for i in range(start - 1, end + 1):
    for j in range(start - 1, end + 1):
        print("{0} x {1} = {2}".format(i, j, i * j))
