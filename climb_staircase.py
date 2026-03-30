n = 2

def climb_staircases(n):
	a, b = 0, 1
	for _ in range(n):
		a , b = b, a+b

	return b

print(climb_staircases(n))
