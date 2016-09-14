#!/bin/python

import sys

def is_weird(n):
    
    if n%2 != 0:
        return True
    
    else:
        if n in range(2, 5+1):
            return False
        if n in range(6, 20+1):
            return True
        if n > 20:
            return False
        
N = int(raw_input().strip())

print "Weird" if is_weird(N) else "Not Weird"
