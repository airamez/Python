"""
Calculate how many minutes a client stayed in a store based on the time (Hour:Minutes) he arrived and the
    time (Hour:Minutes) he left.
    e.g
    INPUT
    Arrived at Hour = 8
    Arrive at Minutes = 15
    Left at Hour = 9
    Left at Minutes = 5
    OUTPUT
    Minutes in store = 50 minutes
"""
arrived_hour = int(input("Arrived at Hour: "))
arrived_minutes = int(input("Arrive at Minutes: "))
left_hour = int(input("Left at Hour: "))
left_minutes = int(input("Left at Minutes: "))

arrived_in_minutes = arrived_hour * 60 + arrived_minutes
left_in_minutes = left_hour * 60 + left_minutes

stayed_in_minutes = left_in_minutes - arrived_in_minutes

print("Minutes in store = ", stayed_in_minutes)

