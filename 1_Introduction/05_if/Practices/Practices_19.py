import random
"""
Write a program to generate a random integer number between 0 and 100 and give the user 5 chances to guess the
number. For every guess inform if the generated number is smaller or greater than the guessed number.
As soon as the user guess the number correctly, stop the game and print a victory message.
If the user doesn't guess the number print a defeat message.
"""

READ_NUMBER_MESSAGE = "Number = "
VICTORY_MESSAGE = "CONGRATULATIONS! YOU WON!"
SMALLER_MESSAGE = "The generated number is smaller"
GREATER_MESSAGE = "The generated number is greater"
LOST_MESSAGE = "SORRY BUT YOU LOST!"

random_number = random.randint(0, 100)
print(random_number)

guess = int(input(READ_NUMBER_MESSAGE))

if guess == random_number:
    print(VICTORY_MESSAGE)
else:
    if guess < random_number:
        print(GREATER_MESSAGE)
    else:
        print(SMALLER_MESSAGE)
    guess = int(input(READ_NUMBER_MESSAGE))
    if guess == random_number:
        print(VICTORY_MESSAGE)
    else:
        if guess < random_number:
            print(GREATER_MESSAGE)
        else:
            print(SMALLER_MESSAGE)
        guess = int(input(READ_NUMBER_MESSAGE))
        if guess == random_number:
            print(VICTORY_MESSAGE)
        else:
            if guess < random_number:
                print(GREATER_MESSAGE)
            else:
                print(SMALLER_MESSAGE)
            guess = int(input(READ_NUMBER_MESSAGE))
            if guess == random_number:
                print(VICTORY_MESSAGE)
            else:
                if guess < random_number:
                    print(GREATER_MESSAGE)
                else:
                    print(SMALLER_MESSAGE)
                guess = int(input(READ_NUMBER_MESSAGE))
                if guess == random_number:
                    print(VICTORY_MESSAGE)
                else:
                    print(LOST_MESSAGE)
