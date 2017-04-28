"""
OR => true when one condition is true
True  or True  = True
False or True  = True
True  or False = True
False or False = False
"""
i_am_sick = input("Are you sick (Y/N)? = ") == "Y"
is_raining = input("Is raining (Y/N)? = ") == "Y"
if i_am_sick or is_raining:
    if i_am_sick:
        print("Go to the doctor.")
    else:
        print("Stay at home.")
else:
    print("Go fishing.")

