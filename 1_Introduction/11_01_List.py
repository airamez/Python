"""
Introduction to collections:
It is really common in coding the requirement to store a collection or list of values.
Every programming language offer many different collection components and the most basic is called Array.
An Array is a collection of elements of a specific type and the size of the array is define on creation and can't be 
changed later.
Most of the "major" programming languages like C, C++, Java and C# offer a basic type for Array. However Python doesn't
offer a basic type matching the classic concept of Arrays. Instead Python offers a Collection called List that is very
powerful and flexible. 
"""
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
print(months)

for i in range(0, 12):
    print(i, "=>", months[i])

month = int(input("Type the number of a month: (1 to 12) = "))
print(months[month-1])
