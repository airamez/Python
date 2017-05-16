"""
Generate and show two integers numbers between 0 and 99, ask the user to try the addition of both numbers
and let the user know if the result is right or not.
"""
import random

MINIMUM = 0
MAXIMUM = 99

number1 = random.randint(MINIMUM, MAXIMUM)
number2 = random.randint(MINIMUM, MAXIMUM)
sum_result = number1 + number2

question = "{0} + {1} = ".format(number1, number2)
guess = int(input(question))

if guess == sum_result:
    print("Congratulations. Your answer is correct!")
else:
    print("Sorry. Your answer is incorrect!")
