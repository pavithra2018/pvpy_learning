"""
    An equilateral triangle is a triangle in which all three sides are equal.
    A scalene triangle is a triangle that has three unequal sides.
    An isosceles triangle is a triangle with (at least) two equal sides.
"""

side1 = int(input("enter side1 value:"))
side2 = int(input("enter side2 value:"))
side3 = int(input("enter side3 value:"))
if (side1 > 0 and side2 > 0 and side3 > 0) :
    if side1 == side2 == side3 :
        print("it is an equilateral triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1 :
        print("it is an isoceles triangle")
    else :
        print("it is a scalane triangle")
else :
    print("sides cannot be negative")
