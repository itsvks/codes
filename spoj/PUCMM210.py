m = int(raw_input().strip())

import time
start = time.clock()

for k in xrange(0, m):
	n = int(raw_input().strip())

	result = n*(n+1)*(2+n*(13+n*(12+n*3)))/60
	print result % 1000000003