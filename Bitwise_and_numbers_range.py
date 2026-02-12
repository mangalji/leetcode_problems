left = 1
right = 2147483647
# res = 1
# for i in range(left,right+1):
# 	res = res & i
# # print(res)
# return res
while left < right:
	right &= right - 1

print(right) 