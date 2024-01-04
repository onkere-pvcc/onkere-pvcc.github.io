#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      adius
#
# Created:     16/09/2023
# Copyright:   (c) adius 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def sum_to(n):
  a = 0
  for i in range(n+1):
    a = a + i
  return a

print(sum_to(10))