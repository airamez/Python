# Reading values with a FLAG
while True:
    number = input("Type a integer number or [Enter] to exit = ")
    if number == "":
        break
    number = int(number)
    print("This is your number = ", number)
print("Bye bye!")
