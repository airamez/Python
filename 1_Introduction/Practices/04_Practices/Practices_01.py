"""
Read the user name and print the message "Hello, USER_NAME"
"""
NAME_INPUT_MESSAGE = "Name: "
MESSAGE_TEMPLATE = "Hello, {0}"

name = input(NAME_INPUT_MESSAGE)
message = MESSAGE_TEMPLATE.format(name)
print(message)
