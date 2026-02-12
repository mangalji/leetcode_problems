# n = 964176192
# n = 2147483644
# n = 43261596
n = int(input("enter the number: "))
res = ''
final_res = 0

while n > 0:
	res = str(n%2) + res
	n = n//2

for i in res:
	if i == '1':
		final_res += 1

# print(final_res)
print(res)
# print(len(res))