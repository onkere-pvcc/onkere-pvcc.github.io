#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adius
#
# Created:     17/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def area_of_circle(r):
    if r < 0:
        return "Radius must be non-negative"
    else:
        return math.pi * r**2

# Example usage:
radius = 5.0  # Replace with your desired radius
circle_area = area_of_circle(radius)
print("The area of the circle with radius", radius, "is", circle_area)
