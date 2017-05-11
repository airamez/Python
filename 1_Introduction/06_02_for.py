start = 1
end = 10
for i in range(start, end + 1):
    print('{0}{1} '.format(i, "," if i != end else ""), end="")
print()

