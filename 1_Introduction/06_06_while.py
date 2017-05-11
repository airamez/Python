start = 1
end = 10

# Prints the number from start to end however removing the last ','
i = start
while i <= end:
    if i < end:
        print("{0}, ".format(i), end="")
    else:
        print(i)
    i += 1
print()
