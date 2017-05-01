start = 1
end = 10

# Prints the number from start to end
i = start
while i <= end:
    print("{0}, ".format(i), end="")
    i += 1
    # Everything aligned/indented inside the while statement is part of the while statement
print()

# Prints the number from start to end however removing the last ','
i = start
while i <= end:
    if i < end:
        print("{0}, ".format(i), end="")
    else:
        print(i)
    i += 1
print()

# while with continue and break
# continue skip the current interaction
# break ends the loop
i = start
while True:
    i += 1
    if i % 2 != 0:
        continue  # Jump to the begin of the while ignore the next statements
    if i >= 10:
        break  # Ends the loop. Move to the next command
    print("{0}, ".format(i), end="")
print()
