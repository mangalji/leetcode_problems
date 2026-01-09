


def set_bit(n):
	result = ''
	final_result = 0

	while n > 0:
		result = str(n%2) + result
		n = n//2

	if result == '0':
		return result
	else:
		for j in result:
			if j == '1':
				final_result += 1
	
	return final_result

ans = []
n = 5
for i in range(n+1):
	a = set_bit(i)
	ans.append(a)

print(ans)
