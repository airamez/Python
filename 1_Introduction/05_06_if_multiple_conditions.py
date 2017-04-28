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
