"""
A function is a block of organized, reusable code that is used to perform a single, related action.
Functions help to keep your code clean, easy to understand,
provide better modularity for your application and a high degree of code reusing.
"""


def average(number1, number2, number3):
    return (number1 * 3 + number2 * 3 + number3 * 4) / 10

print(average(5, 5, 8))
print(average(8, 8, 5))
print(average(number3=8, number1=8, number2=5))

num1 = int(input("Number 1 = "))
num2 = int(input("Number 2 = "))
num3 = int(input("Number 3 = "))

avg = average(num1, num2, num3)
print(avg)

avg = average(number1=num1, number2=num2, number3=num3)
print(avg)

avg = average(number1=num3, number2=num2, number3=num1)
print(avg)
