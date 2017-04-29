gender = input("What is your gender? (M/F): ")
if gender == 'M':
    hasGirlfriend = input("Do you have a girlfriend? (Y/N): ")
    if hasGirlfriend == "Y":
        girlfriendName = input("What is you girlfriend name: ")
        print(girlfriendName, "is a luck woman")
    else:
        print("So sorry for you")
elif gender == 'F':
    hasBoyfriend = input("Do you have a boyfriend? (Y/N): ")
    if hasBoyfriend == "Y":
        boyfriendName = input("What is you boyfriend name: ")
        print(boyfriendName, "is a luck man")
    else:
        print("So sorry for you")
else:
    print("Wrong gender")
print("Have a nice day")
