import random

rnd = random.randint(1, 10)

# Option 1
guess = int(input("Type a number between 1 and 10 = "))
while guess != rnd:
    guess = int(input("Type a number between 1 and 10 = "))

print("Congratulations! You found the number: {0}".format(rnd))

