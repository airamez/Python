"""
Read three values and indicate if they can form a triangle.
"""
side_a = float(input("Side A = "))
side_b = float(input("Side B = "))
side_c = float(input("Side C = "))

# Option 1
if side_a < side_b + side_c and side_b < side_a + side_c and side_c < side_a + side_b:
    print("Triangle")
else:
    print("Not Triangle")

# Option 2
if side_a >= side_b + side_c or side_b >= side_a + side_c or side_c >= side_a + side_b:
    print("Not Triangle")
else:
    print("Triangle")
