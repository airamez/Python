# Reading values with a FLAG
while True:
    number = input("Type a integer number or [Enter] to exit = ")
    if number:  # Anything different of False, None, 0, "", (), [], {} is True
        number = int(number)
        print("This is your number = ", number)
    else:  # All these values are False: False, None, 0, "", (), [], {}
        break
print("Bye bye!")
