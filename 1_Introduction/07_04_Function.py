def read_integer(message: str = 'Type an integer number = '):
    """
    Reads a integer number
    :param message: message
    :return: The integer number
    """
    value = int(input(message))
    return value


int1 = read_integer()
print(int1)
age = read_integer("Type your age = ")
print(age)

