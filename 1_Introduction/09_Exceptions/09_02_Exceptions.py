"""
It is possible to catch multiple exceptions 
"""


def my_division(number_1, number_2) -> float:
    try:
        return float(number_1) / float(number_2)
    except ValueError:
        print("Invalid parameters: {0}/{1}".format(number_1, number_2))
    except ZeroDivisionError:
        print("Division by zero: {0}/{1}".format(number_1, number_2))

print('my_division(10, 4) =', my_division(10, 4))
print('my_division("Python", 2) =', my_division("Python", 2))
print('my_division(10, 0) =', my_division(10, 0))

while True:
    try:
        number1 = input("Number 1 = ")
        number2 = input("Number 2 = ")
        division = my_division(number1, number2)
        if division:
            print("Division = ", division)
            break
    except:
        pass  # This means we don't want to do anything if there is an exception
