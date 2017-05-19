"""
Read a time defined as Hour and Minutes where the Hour will be in military format (0 to 23) and print the time
as conventional hour representation: Hour:Minutes AM/PM.
    e.g.
    Hour: 17
    Minutes: 45
    Conventional hour = 5:45 PM
"""

hour = int(input("Hour = "))
minutes = int(input("Minutes = "))

if hour <= 11:
    am_pm = "am"
elif hour == 12:
    am_pm = "pm"
else:
    hour -= 12
    am_pm = "pm"

print("{0}:{1}{2}".format(hour, minutes, am_pm))


