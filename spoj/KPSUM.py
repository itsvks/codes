n = int(raw_input().strip())

def calculate_sum(n, start):
	if n >= 10:
		tc = 0
		for index, val in enumerate(map(int, str(n))):
			if start == 'minus':
				if index%2 == 0:
					tc = tc - val
				else:
					tc = tc + val

			if start == 'plus':
				if index%2 == 0:
					tc = tc + val
				else:
					tc = tc - val
		return tc * -1
	return n

for i in range(1, n+1):
	total_sum = 0

	for i in range(1, i+1):
		if i%2 == 0:
			total_sum = total_sum - calculate_sum(i, 'minus')
		else:
			total_sum = total_sum + calculate_sum(i, 'plus')

	print total_sum