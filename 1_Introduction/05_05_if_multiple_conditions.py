"""
AND => true when all conditions are true
True  and True  = True
False and true  = False
True  and False = False
False and False = False
"""

print("# Option 1")
is_weekend = input("Is Weekend (Y/N)? = ")
if is_weekend == "Y":
    is_raining = input("Is raining (Y/N)? = ")
    is_wife_busy = input("Is wife busy (Y/N)? = ")
    if is_raining == "N" and is_wife_busy == "Y":
        print("Go fishing!")
    elif is_wife_busy == "N":
        print("Go grocery with wife")
    else:
        print("Prepare coding classes")
else:
    print("Go to work!")

print("# Option 2")
is_weekend = input("Is Weekend (Y/N)? = ") == "Y"
if is_weekend:
    is_raining = input("Is raining (Y/N)? = ") == "Y"
    is_wife_busy = input("Is wife busy (Y/N)? = ") == "Y"
    if (not is_raining) and is_wife_busy:
        print("Go fishing!")
    elif not is_wife_busy:
        print("Go grocery with wife")
    else:
        print("Prepare coding classes")
else:
    print("Go to work!")
