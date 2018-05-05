"""
02. Read two integer numbers representing an interval and print all numbers inside the interval.
"""

start = int(input('Start = '))
end = int(input('End = '))

if start < end:
    for n in range(start + 1, end):
        print(str(n) + ' ', end='')
else:
    for n in range(start - 1, end, -1):
        print(str(n) + ' ', end='')
