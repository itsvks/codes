import sys

def get_number_of_pairs(a, n, k):
	number_of_pairs = 0
	for i in range(n):
		for j in range(i+1, n):
			if (a[i] + a[j]) % k == 0:
				number_of_pairs = number_of_pairs + 1
	return number_of_pairs


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))
print get_number_of_pairs(a, n, k)
