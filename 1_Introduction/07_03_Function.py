"""
Functions with typed parameters and typed return
"""


def get_salutation(name: str, hour: int) -> str:  # Providing the type of the parameters and return type
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


# Control + Q shows documentation
print(get_salutation("José", 8))
print(get_salutation("Artur", 13))
print(get_salutation("Leila", 18))
print(get_salutation("Nilzete", 22))

# Passing parameters by name. This ignore the order
print(get_salutation(name="Alciene", hour=7))
print(get_salutation(hour=15, name="Zenilton"))

# Passing variables as parameters
myName = "José"
myHour = 15
print(get_salutation(myName, myHour))
print(get_salutation(hour=myHour, name=myName))

myName = input("Name = ")
myHour = int(input("Hour = "))
mySalutation = get_salutation(myName, myHour)
print(mySalutation)
