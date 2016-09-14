def hotness(l1, l2):
	return reduce(lambda x,y: x+y, map(lambda x,y:x*y, l1, l2))

n = int(raw_input().strip())
count = 0

while count < n:
	m = int(raw_input().strip())
	l1 = sorted(map(int, raw_input().strip().split(' ')))
	l2 = sorted(map(int, raw_input().strip().split(' ')))
	print hotness(l1, l2)
	count += 1
