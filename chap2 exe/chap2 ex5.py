#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adius
#
# Created:     03/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math


radius = 10
length_rectangle = 10
height_rectangle = 5
base_triangle = 10
height_triangle = 5

area_circle = math.pi * (radius ** 2)
area_rectangle = length_rectangle * height_rectangle
area_triangle = 0.5 * base_triangle * height_triangle

print(f"Area of the circle with a radius of {radius} is {area_circle:.2f}")
print(f"Area of the rectangle with a length of {length_rectangle} and height of {height_rectangle} is {area_rectangle}")
print(f"Area of the triangle with a base of {base_triangle} and height of {height_triangle} is {area_triangle}")
