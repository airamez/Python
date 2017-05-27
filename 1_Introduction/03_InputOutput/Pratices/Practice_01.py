'''
1. Write a program to read the area code, the prefix and a phone number and print
   the full phone number using the formatting: (999) 999-9999
'''

# Data entry
areaCode = input("Area Code: ")
prefix = input("Prefix: ")
number = input("Number: ")

# Case 1
print("(", areaCode, ")", prefix, "-", number)

# Case 2
print("(", end='')
print(areaCode, end='')
print(") ", end='')
print(prefix, end='')
print("-", end='')
print(number)

# Case 3
fullPhoneNumber = "(" + areaCode + ") " + prefix + "-" + number
print(fullPhoneNumber)

# Case 4
fullPhoneNumber = "({0}) {1}-{2}".format(areaCode, prefix, number)
print(fullPhoneNumber)

# Case 5
fullPhoneNumber = "({AREA_CODE}) {PREFIX}-{PHONE_NUMBER}".format(AREA_CODE=areaCode, PREFIX=prefix, PHONE_NUMBER=number)
print(fullPhoneNumber)
