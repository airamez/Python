"""
Generate a basic random operation of addition, subtraction, multiplication or division using two integer numbers
from 0 to 99 and challenge the user for the right answer.
Let the user know if the guess is correct or incorrect.
e.g
34 x 12 = 408
Congratulations, your answer is correct!
"""
import random

number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# 1 = Addition; 2 = Subtraction; 3 = Multiplication; 4 = Division
operation = random.randint(1, 4)

result = None
operationText = None

if operation == 1:
    operationText = "+"
    result = number1 + number2
elif operation == 2:
    operationText = "-"
    result = number1 - number2
elif operation == 3:
    operationText = "x"
    result = number1 * number2
else:
    if number2 == 0:
        number2 = 1
    operationText = "÷"
    result = number1 // number2

question = "{0} {1} {2} = ".format(number1, operationText, number2)
answer = int(input(question))

if answer == result:
    print("Congratulations. Your answer is CORRECT!")
else:
    print("Sorry. Your answer is INCORRECT!.")
    print("The correct answer is {0}".format(result))
