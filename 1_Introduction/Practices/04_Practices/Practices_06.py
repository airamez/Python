"""
Read an temperature value in Fahrenheit and calculate it correspondent value in Celsius.
Source: http://www.rapidtables.com/convert/temperature/how-fahrenheit-to-celsius.htm
Formula: T(°C) = (T(°F) - 32) / 1.8
"""

Fahrenheit = int(input("Fahrenheit = "))
Celsius = round((Fahrenheit - 32) / 1.8, 2)
print("Celsius", Celsius, "°C")
