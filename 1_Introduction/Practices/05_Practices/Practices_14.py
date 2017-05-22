"""
Read a time as Hour, Minute and a Complement (am/pm) and print the time in a military format.
    e.g.
    Hour: 3
    Minutes: 45
    Complement: pm
    Military time = 15:45
"""

hour = int(input("Hour: "))
minutes = int(input("Minutes: "))
complement = input("Complement (am/pm): ")

# Option 1
if complement == "am":
    print("{0}:{1}".format(hour, minutes))
elif hour == 12 and complement == "pm":
    print("{0}:{1}".format(hour, minutes))
elif hour != 12 and complement == "pm":
    print("{0}:{1}".format(hour + 12, minutes))

# Option 2
if complement == "am" or hour == 12:
    print("{0}:{1}".format(hour, minutes))
else:
    print("{0}:{1}".format(hour + 12, minutes))

# Option 3
hour_military = None
minutes_military = None
if complement == "am" or hour == 12:
    hour_military = hour
    minutes_military = minutes
else:
    hour_military = hour + 12
    minutes_military = minutes
print("{0}:{1}".format(hour_military, minutes_military))

# Option 4: We just need to change the hour by adding 12 when is PM and hour is not 12
if hour != 12 and complement == "pm":
    hour += 12
print("{0}:{1}".format(hour, minutes))


