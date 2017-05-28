start = 1

# while with continue and break:
#   continue - skip the current interaction
#   break - ends the loop
i = start
while True:
    i += 1
    if i % 2 != 0:
        continue  # Jump to the begin of the while ignoring the next statements
    if i >= 50:
        break  # Ends the loop. Move to the next command (The one after thw while)
    print("{0}, ".format(i), end="")
print()
