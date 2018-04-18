start = 1
end = 20

# Printing the numbers from start to end informing if it is odd or even
i = start
while i <= end:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i += 1
print("This is a command after the while")
