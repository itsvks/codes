def square(x):
    return int(x) * int(x)

def happy(number):
    return sum(map(square, list(str(number))))

def is_happy(number):
    count = 0
    seen_numbers = set()
    while number > 1 and (number not in seen_numbers):
        seen_numbers.add(number)
        number = happy(number)
        count += 1
    return number == 1, count

n = int(raw_input().strip())
status, count = is_happy(n)
if status:
	print count
else:
	print -1
