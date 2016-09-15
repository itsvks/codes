#!/bin/python

import sys


def get_maximum_hourglass_sum(arr):
    
    max_sum = sum([arr[1][1], arr[1-1][1-1], arr[1-1][1], arr[1-1][1+1], arr[1+1][1-1], arr[1+1][1], arr[1+1][1+1]]) 

    for i in xrange(1, 5):
        for j in xrange(1, 5):
            temp_sum = sum([arr[i][j], arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1]]) 
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

print get_maximum_hourglass_sum(arr)
