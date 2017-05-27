"""
Check if a Year is a Leap Year
A year is a leap year if it is divisible by 4 but not for 100 however it is leap if it divisible by 400

There are 30 leap years between 1900 and 2020:
1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 
1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020.
"""
year = int(input("Year = "))

divisible_by_4 = year % 4 == 0
divisible_by_100 = year % 100 == 0
divisible_by_400 = year % 400 == 0

# Method 1
if not divisible_by_4:
    print("NOT Leap Year")
elif divisible_by_400:
    print("Leap Year")
elif divisible_by_100:
    print("NOT Leap Year")
else:
    print("Leap Year")

# Method 2
if not divisible_by_4:
    print("NOT Leap Year")
elif divisible_by_100 and not divisible_by_400:
    print("NOT Leap Year")
else:
    print("Leap Year")

# Method 3
if (divisible_by_4 and not divisible_by_100) or divisible_by_400:
    print("Leap Year")
else:
    print("NOT Leap Year")

# Method 4
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("NOT Leap Year")
