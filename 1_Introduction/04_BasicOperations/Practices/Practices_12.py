"""
12. Calculate how many dollar's bills of each one of the following values ($1, $5, $10, $20, $50) should be released
    in an ATM machine for a withdraw operation.
    The ATM machine should always give less dollar's bills as possible
    e.g. INPUT
      Value = 1,338.00
    OUTPUT
      50 bills = 26
      20 bills = 1
      10 bills = 1
       5 bills = 1
       1 bills = 3
"""
value = int(input("Withdraw value: "))
valueAux = value

# Method 1
bills50 = valueAux // 50
valueAux = valueAux % 50
bills20 = valueAux // 20
valueAux = valueAux % 20
bills10 = valueAux // 10
valueAux = valueAux % 10
bills5 = valueAux // 5
bills1 = valueAux % 5

print("50 bills =", bills50)
print("20 bills =", bills20)
print("10 bills =", bills10)
print(" 5 bills =", bills5)
print(" 1 bills =", bills1)

# Method 2
valueAux = value
div = divmod(valueAux, 50)
bills50 = div[0]
div = divmod(div[1], 20)
bills20 = div[0]
div = divmod(div[1], 10)
bills10 = div[0]
div = divmod(div[1], 5)
bills5 = div[0]
bills1 = div[1]

print("50 bills =", bills50)
print("20 bills =", bills20)
print("10 bills =", bills10)
print(" 5 bills =", bills5)
print(" 1 bills =", bills1)

# Method 3
bills50 = value // 50
bills20 = (value % 50) // 20
bills10 = ((value % 50) % 20) // 10
bills5 = (((value % 50) % 20) % 10) // 5
bills1 = (((value % 50) % 20) % 10) % 5

print("50 bills =", bills50)
print("20 bills =", bills20)
print("10 bills =", bills10)
print(" 5 bills =", bills5)
print(" 1 bills =", bills1)
