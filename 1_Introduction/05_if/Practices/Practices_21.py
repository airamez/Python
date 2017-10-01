"""
Read two intervals of integer numbers represented by four values
(interval_1_min, interval_1_max, interval_2_min and interval_2_max)
and indicate which of the following
positions the interval 1 is related to the interval 2:
ALL-LEFT     = All on the left
LEFT-MIDDLE  = Starts on the left but ends in the middle
ALL-MIDDLE   = Starts and ends inside the middle
MIDDLE_RIGHT = Starts in the middle and ends on the right
ALL-RIGHT    = All on the right
"""

interval_1_min = int(input("Interval 1 minimum: "))
interval_1_max = int(input("Interval 1 maximum: "))
interval_2_min = int(input("Interval 2 minimum: "))
interval_2_max = int(input("Interval 2 maximum: "))

if interval_1_max < interval_2_min:
    print("ALL-LEFT")
elif interval_1_min < interval_2_min and interval_1_max < interval_2_max:
    print("LEFT-MIDDLE")
elif interval_1_min >= interval_2_min and interval_1_max <= interval_2_max:
    print("ALL-MIDDLE")
elif interval_2_min <= interval_1_min < interval_2_max < interval_1_max:
    print("MIDDLE_RIGHT")
else:
    print("ALL-RIGHT")
