nums = [0,1,0,3,12]

for num in nums:
	if num == 0:
		nums.remove(num)
		nums.append(num)
print(nums)