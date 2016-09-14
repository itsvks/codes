#!/usr/bin/python

import sys

time = raw_input().strip()

converted_time = time[:-2]

h_m_s_list = time[:-2].split(':')

if time[-2:] == 'PM' and h_m_s_list[0] != '12':
	converted_time = str(int(h_m_s_list[0]) + 12) + ":" + h_m_s_list[1] + ":" + h_m_s_list[2]

if time[-2:] == 'AM' and h_m_s_list[0] == '12':
	converted_time = '00' + ":" + h_m_s_list[1] + ":" + h_m_s_list[2]

print converted_time
