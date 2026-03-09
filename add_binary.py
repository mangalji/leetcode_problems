a = '1010'
b = '1011'
# outout = '100'
'''

decimal_a = int(a,2)
decimal_b = int(b,2)

decimal = decimal_a + decimal_b

# decimal_string = str(decimal)
res = ''

while decimal > 0:
	res = str(decimal%2) + res
	decimal = decimal // 2

print(res)'''

# optimized solution:

def addbinary(a,b):
	result = []
	carry = 0
	i,j = len(a) - 1, len(b) - 1

	while i >= 0 or j >= 0 or carry:
		bit_a = int(a[i]) if i >= 0 else 0
		bit_b = int(b[j]) if j >= 0 else 0
	
		total = bit_a + bit_b + carry
	
		result.append(str(total%2))
		carry = total//2
	
		i -= 1
		j -= 1
	return ''.join(reversed(result))

print(addbinary(a,b))