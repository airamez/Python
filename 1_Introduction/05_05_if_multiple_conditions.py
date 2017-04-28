"""
AND => true when all conditions are true
True  and True  = True
False and true  = False
True  and False = False
False and False = False
"""
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

