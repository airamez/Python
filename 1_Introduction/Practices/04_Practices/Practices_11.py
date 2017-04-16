"""
Same as the previous question however calculating the time the client stayed in the story as hour:minutes
    INPUT
    Arrived at Hour = 8
    Arrived at Minutes = 15
    Left at Hour = 10
    Left at Minutes = 45
    OUTPUT
    Minutes in store = 2:30
"""
arrived_hour = int(input("Arrived at Hour: "))
arrived_minutes = int(input("Arrive at Minutes: "))
left_hour = int(input("Left at Hour: "))
left_minutes = int(input("Left at Minutes: "))

arrived_in_minutes = arrived_hour * 60 + arrived_minutes
left_in_minutes = left_hour * 60 + left_minutes

stayed_in_minutes = left_in_minutes - arrived_in_minutes

hour = stayed_in_minutes // 60
minutes = stayed_in_minutes % 60
print("{0}:{1}".format(hour, minutes))

time = divmod(stayed_in_minutes, 60)
print("{0}:{1}".format(time[0], time[1]))
