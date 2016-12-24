# INPUT
name = input("Type your name: ")  # The input command always returns an string
print("Hello " + name + ", welcome to the Learning Python course")

age = int(input("What is your age: "))  # As we want an integer we need to convert the result of the input to int
print(age)

payment = float(input("Payment value: "))  # Converting the input to float
print(payment)

# Printing 3 variables
print(name, age, payment)

# Printing with descriptions
print("Name =", name, "; Age =", age, "; Payment =", payment)

# Printing using format (parameters by order)
message = "Name = {0}; Age = {1}; Payment = {2}".format(name, age, payment)
print(message)

# Printing using format (parameters by name)
message = "Name = {name}; Age = {age}; Payment = {payment}".format(payment=payment, age=age, name=name)
print(message)

# If we want to print without move to a new line
print('1', end='')
print('2', end='')
print('3', end='')
print('4', end='')
print('5', end='')

print("Practices")

