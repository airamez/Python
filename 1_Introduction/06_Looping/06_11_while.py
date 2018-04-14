# while with continue and break:
# continue = skip the current interaction
# break = ends the loop

i = 0
"""
Print all even numbers from 1 to 50
"""
while True:  # Lopping forever. A break statement is required to finish the loop
    i += 1
    if i % 2 != 0:
        continue  # Jump to the begin of the while ignoring the next statements
    if i > 50:
        break  # Ends the loop. Move to the next command (The one after the while)
    print("{0} ".format(i), end="")
print("\nThis is a command after the while")

