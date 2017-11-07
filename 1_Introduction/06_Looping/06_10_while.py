start = 1
end = 10

# Printing the numbers from start to end in the same line however removing the last ','
i = start
while i <= end:
    if i < end:
        print("{0}, ".format(i), end="")
    else:
        print(i)
    i += 1
print("This is a command after the while")
