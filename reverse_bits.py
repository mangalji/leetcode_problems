n = 43261596
res = ''
while n > 0:
	res = str(n%2) + res
	n = n // 2

# reverse_res = res[::-1]
b = res[::-1]


if len(res) < 32:
	a = 32 - len(res)
	for i in range(a):
		b += '0'
# print(len(res))
# reverse_res = b[::-1]
print(b)


# print(res)
# print(reverse_res)
print(int(b,2))

# binary = '110001010'
# decimal = 0
# for digit in binary:
#     decimal = decimal*2 + int(digit)
# print(decimal)
# binary = '110001011'
# print(int(binary,2))