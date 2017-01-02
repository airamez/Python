"""
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions help to keep your code clean, easy to understand,
provide better modularity for your application and a high degree of code reusing.
"""


def average(number1, number2, number3):
    return (number1 * 3 + number2 * 3 + number3 * 4) / 10

print(average(5, 5, 8))
print(average(8, 8, 5))
print(average(number3=8, number1=8, number2=5))


def repeat(string, times=10):  # Default parameter
    result = ''
    for i in range(1, times + 1):
        result = result + string
    return result

print(repeat('*'))
print(repeat('*', 5))
print(repeat('*', 1))
print(repeat('=', 80))
print(repeat(' ', 35), end='')
print('This is a function')
print(repeat('=', 80))


def get_salutation(name: str, hour: int) -> str:
    """
    This function returns the proper salutation based on the hour
    :param name: Name
    :param hour: Hour
    :return: Proper salutation for the hour
    """
    if hour <= 12:
        salutation = "Good morning"
    elif hour <= 14:
        salutation = "Good afternoon"
    elif hour <= 20:
        salutation = "Good evening"
    else:
        salutation = "Good night"
    return "Hello {0}, {1}".format(name, salutation)


print(get_salutation("José", 8))
print(get_salutation("Artur", 13))
print(get_salutation("Leila", 18))
print(get_salutation("Nilzete", 22))

myName = "José"
myHour = 15
print(get_salutation(myName, myHour))
print(get_salutation(hour=myHour, name=myName))


print("Practices")
