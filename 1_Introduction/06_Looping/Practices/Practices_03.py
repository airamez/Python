"""
03. Read two integer numbers representing an interval and print all even numbers inside the interval.
"""

start = int(input('Start = '))
end = int(input('End = '))

# Solution 1
increment = 1
if start > end:
    increment = -1
for n in range(start + increment, end, increment):
    if n % 2 == 0:
        print(str(n) + ' ', end='')
print()

# Solution 2
if start < end:
    increment = 2
    if start % 2 == 0:
        start += 2
    else:
        start += 1
else:
    increment = -2
    if start % 2 == 0:
        start -= 2
    else:
        start -= 1

for n in range(start, end, increment):
    print(str(n) + ' ', end='')
