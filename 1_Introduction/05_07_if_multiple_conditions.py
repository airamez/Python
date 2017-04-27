"""
Check if a Year is a Leap Year
A year is a leap year if it is divisible by 4 but not for 100 however it is leap if it divisible by 400
"""
year = int(input("Year = "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("NOT Leap Year")
