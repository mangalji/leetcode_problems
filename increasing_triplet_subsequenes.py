# nums = [5,4,3,2,1]
# nums = [2,1,5,0,4,6]
# nums = [1,2,3,4,5]
nums = [20,100,10,12,5,13]

if len(nums) < 3:
	print(False)
i = float('inf')
j = float('inf')

for num in nums:
	if num<=i:
		i=num
	elif num<=j:
		j=num
	else:
		print(True)
print(False)

