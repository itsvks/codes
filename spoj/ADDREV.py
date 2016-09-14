n = int(raw_input().strip())

for k in range(0, n):
	m = raw_input().strip()

	m = m.split(" ")

	sum = int(m[0][::-1]) + int(m[1][::-1])

	print str(sum)[::-1].lstrip("0")