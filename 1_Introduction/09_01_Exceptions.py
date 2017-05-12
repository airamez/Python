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
