start = 1
end = 10

# Printing the numbers from start to end however in the same line and removing the last ','
i = start
while i <= end:
    if i < end:
        print("{0}, ".format(i), end="")
    else:
        print(i)
    i += 1
print("This is a command after the while")
