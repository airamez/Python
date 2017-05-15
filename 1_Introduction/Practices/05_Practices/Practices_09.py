"""
Read three values and indicate if they can form a triangle and what type of triangle it would be:
Equilateral, Isosceles, Scalene.
"""
side_a = float(input("Side A = "))
side_b = float(input("Side B = "))
side_c = float(input("Side C = "))

if side_a < side_b + side_c and \
   side_b < side_a + side_c and \
   side_c < side_a + side_b:

    # Option 1
    print("Triangle")
    if side_a == side_a and side_a == side_c and side_b == side_c:
        print("Equilateral")
    if (side_a == side_b and side_a != side_c and side_b != side_c) or \
       (side_a == side_c and side_a != side_b and side_c != side_b) or \
       (side_b == side_c and side_b != side_a and side_c != side_a):
        print("Isosceles")
    if side_a != side_b and side_a != side_c and side_b != side_c:
        print("Scalene")

    # Option 2
    if side_a == side_a and side_a == side_c and side_b == side_c:
        print("Equilateral")
    elif (side_a == side_b and side_a != side_c and side_b != side_c) or \
         (side_a == side_c and side_a != side_b and side_c != side_b) or \
         (side_b == side_c and side_b != side_a and side_c != side_a):
        print("Isosceles")
    elif side_a != side_b and side_a != side_c and side_b != side_c:
        print("Scalene")

    # Option 3
    if side_a == side_b and side_a == side_c:
        print("Equilateral")
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not Triangle")
