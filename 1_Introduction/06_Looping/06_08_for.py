# for with continue and break:
# continue = skip the current interaction
# break = ends the loop

print('continue example')
for i in range(1, 10):
    if 4 < i < 8:
        continue
    print(i)

print('continue and break example')
for i in range(1, 1000):
    if i == 2 or i == 4:
        continue
    if i == 5:
        break
    print(i)
print('After the for command')
