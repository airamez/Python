age = input('Type your age: ')
age = int(age)

# if
if age >= 18:
    print('----------------')
    print("You are an adult")
    print('----------------')
    # Everything align inside the if statement is part of the if statement
    # Python uses indentation to define statement blocks. Many others languages use open and close delimiters

# if/else
if age < 18:
    print("Your are a kid")
else:
    print("Your are an adult")

# if/elif/else
result = None
if age <= 0:
    result = "fetus/unborn"
elif age <= 1:
    result = "infant"
elif age <= 12:
    result = "kid"
elif age <= 18:
    result = "teenage"
elif age <= 40:
    result = "adult"
elif age <= 60:
    result = "senior"
else:
    result = "old"

print('Your are', result)

# inline if
print("Adult" if age >= 18 else "Young")

# nested ifs
gender = input("What is your gender? (M/F):")
if gender == 'M':
    hasGirlfriend = input("Do you have a girlfriend? (Y/N)")
    if hasGirlfriend == "Y":
        girlfriendName = input("What is you girlfriend name: ")
        print(girlfriendName + " is a luck woman")
    else:
        print("So sorry for you")
elif gender == 'F':
    hasBoyfriend = input("Do you have a boyfriend? (Y/N)")
    if hasBoyfriend == "Y":
        boyfriendName = input("What is you boyfriend name: ")
        print(boyfriendName + " is a luck man")
    else:
        print("So sorry for you")
else:
    print("Wrong gender")

print("Practices")
