#!/usr/bin/python
# -*- coding: utf-8 -*-

'''

Given a time in -hour AM/PM format, convert it to military (-hour) time.

Note: Midnight is  on a -hour clock, and  on a -hour clock. Noon is  on a -hour clock, and  on a -hour clock.


Input Format

A single string containing a time in -hour clock format (i.e.:  or ), where  and .

Output Format

Convert and print the given time in -hour format, where .


Sample Input

07:05:45PM

Sample Output

19:05:45

'''

import sys

time = raw_input().strip()

converted_time = time[:-2]

h_m_s_list = time[:-2].split(':')

if time[-2:] == 'PM' and h_m_s_list[0] != '12':
	converted_time = str(int(h_m_s_list[0]) + 12) + ":" + h_m_s_list[1] + ":" + h_m_s_list[2]

if time[-2:] == 'AM' and h_m_s_list[0] == '12':
	converted_time = '00' + ":" + h_m_s_list[1] + ":" + h_m_s_list[2]

print converted_time
