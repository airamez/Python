# Reading values with a FLAG
while True:
    number = input("Type a integer number or [Enter] to exit = ")
    if number == "":  # If the user type <Enter> without anything else the number will be an empty string
        break
    number = int(number)
    print("This is your number = ", number)
print("Bye bye!")
