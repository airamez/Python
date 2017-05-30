# for using range [start, end[
for i in range(1, 10):
    print(i)
    # All commands aligned inside the for it part of the for looping

for i in range(1, 10):
    print("{0}, ".format(i), end="")

print()
for i in range(1, 10):
    if i < 9:  # Adding the "," after all number but not the last one
        print("{0}, ".format(i), end="")
    else:
        print(i)
