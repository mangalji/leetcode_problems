# nums = [2,7,11,15]
nums = [3,2,4]
# nums = [2,5,5,11]
# nums = [3,3]
target = 6
def two_sum(nums,target):
	index_arr = []
	for i in range(len(nums)):
		for j in range(i+1,len(nums)):
			if (nums[i] + nums[j]) == target:
				index_arr.append(i)
				index_arr.append(j)
				return index_arr

# print(two_sum(nums,target))

def two_sums(nums,target):
	index_arr = []
	for i in range(len(nums)):
		if (nums[i] +nums[i+1]) == target:
			index_arr.append(i)
			index_arr.append(i+1)
			return index_arr 

print(two_sums(nums,target))