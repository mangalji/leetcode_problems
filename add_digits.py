# 258. Add Digits
num = 447

def add_digits(num):

	if num < 0:
		num = abs(num)

	return 0 if num == 0 else (num - 1) % 9 + 1


print(add_digits(num))