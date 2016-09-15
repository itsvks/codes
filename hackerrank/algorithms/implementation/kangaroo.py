#!/bin/python

import sys

def can_land_on_the_same_location(x1, v1, x2, v2):

	if x1 == x2:
		return "YES"

	if (x1 > x2 and v1 >= v2) or (x1 < x2 and v1 <= v2):
		return "NO"

	if (x1 > x2 and v1 <= v2) or (x1 < x2 and v1 >= v2):
		return can_land_on_the_same_location(x1+v1, v1, x2+v2, v2)


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
print can_land_on_the_same_location(x1, v1, x2, v2)
