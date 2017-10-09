import random

rnd = random.randint(1, 10)

# do while simulation
while True:
    guess = int(input("Type a number between 1 and 10 = "))
    if guess == rnd:
        print("Congratulations! You found the number: {0}".format(rnd))
        break
