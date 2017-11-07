# for with continue and break:
# continue = skip the current interaction
# break = ends the loop

for i in range(1, 100):
    if i == 2 or i == 4:
        continue
    if i == 5:
        break
    print(i)
