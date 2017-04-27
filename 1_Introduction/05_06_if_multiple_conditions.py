"""
OR => true when one condition is true
True  or True  = True
False or True  = True
True  or False = True
False or False = False
"""
am_i_sick = input("Are you sick (Y/N)? = ") == "Y"
is_raining = input("Is raining (Y/N)? = ") == "Y"
if am_i_sick or is_raining:
    print("Stay at home")
elif am_i_sick:
    print("Go see the doctor")
else:
    print("Prepare coding classes")

