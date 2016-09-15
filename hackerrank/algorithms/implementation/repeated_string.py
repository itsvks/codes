#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())
a_count = s.count("a") 
print (a_count * (n // len(s))) + s[:n % len(s)].count("a")
