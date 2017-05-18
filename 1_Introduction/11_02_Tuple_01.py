"""
A tuple is basic the same as a list however the elements are immutable.
Tuples are used for grouping data
"""
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print(months)

print(months[0], "..", months[len(months) - 1])

# trying to change a tuple element
try:
    months[1] = "JAN"
except TypeError as e:
    print(e)

while True:
    month = input("Month (ENTER to exit)= ")
    if month == "":
        break
    month = int(month)
    if 1 <= month <= 12:
        print(months[month-1])
    else:
        print("Invalid month")
