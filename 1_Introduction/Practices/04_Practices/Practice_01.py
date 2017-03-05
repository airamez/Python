'''
01. Read the user name and print the message "Hello, USER_NAME"
'''

user_name = input("User Name: ")
print("Hello,", user_name)

greetings = "Hello, " + user_name
print(greetings)

greetings = "Hello, {0}".format(user_name)
print(greetings)
