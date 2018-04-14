"""
Read day, month and year as integers and indicate if the values represent a valid date.

# Basic checks
Day:  [1..31]
Month: [1.12]
Year: > 1900

# Specific checks
Months with 31 days: 1, 3, 5, 7, 8, 10, 12
Months with 30 days: 4, 6, 9, 11
Month with 28 or 29: 2
  29 when leap year: (divisible by 4 and not divisible by 100) or divisible by 400
  20 regular year
"""

VALID_DATE = "Valid Date"
INVALID_DATE = "Invalid Date"

day = int(input("Day = "))
month = int(input("Month = "))
year = int(input("Year = "))

basic_check = True

# Basic checks
if day < 1 or day > 31:
    print(INVALID_DATE, "Day =", day)
    basic_check = False
if month < 1 or month > 12:
    print(INVALID_DATE, "Month =", month)
    basic_check = False
if year < 1900:
    print(INVALID_DATE, "Year =", year)
    basic_check = False

#
#  Specific checks
#

if basic_check:
    if month == 4 or month == 6 or month == 9 or month == 11:
        if 1 <= day <= 30:
            print(VALID_DATE)
        else:
            print(INVALID_DATE)
    # Month with 28 or 29 days
    elif month == 2:
        # Check if is leap Year
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if 1 <= day <= 29:
                print(VALID_DATE)
            else:
                print(INVALID_DATE)
        else:
            if 1 <= day <= 28:
                print(VALID_DATE)
            else:
                print(INVALID_DATE)
    else:  # Months with 31 days. No need to check because passed the basic checks
        print(VALID_DATE)
