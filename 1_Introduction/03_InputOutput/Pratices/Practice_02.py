'''
Write a program to read the year, month and day and print the date using the formatting: dd/mm/yyyy
'''
year = input("Year: ")
month = input('Month: ')
day = input("Day: ")

# Option 1
print(day + "/" + month + "/" + year)

# Option 2
date = day + "/" + month + "/" + year
print(date)

# Option 3
date = "{0}/{1}/{2}".format(day, month, year)
print(date)

# Option 4
date = "{DAY}/{MONTH}/{YEAR}".format(DAY=day, MONTH=month, YEAR=year)
print(date)
