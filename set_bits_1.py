n = 2147483645
res = ''
final_res = 0

while n > 0:
	res = str(n%2) + res
	n = n//2

for i in res:
	if i == '1':
		final_res += 1

print(final_res)