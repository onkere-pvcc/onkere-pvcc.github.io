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

P = 10000
n = 12
r = 0.08


t = int(input("Enter the number of years: "))

A = P * (1 + r/n) ** (n*t)

print(f"The final amount after {t} years will be ${A:.2f}")
