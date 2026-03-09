nums = [1,3,5,6]
target = 6
# def search_insert(nums,target):
# 	for i in range(len(nums)):
# 		if nums[i] == target:
# 			return nums.index(target)
	
# 	for j in range(len(nums)):
# 		if nums[j] >= target:
# 			index = nums.index(nums[j])
# 			insert = nums.insert((index),target)
# 			return nums.index(target)

# 	nums.append(target)
# 	return nums.index(target)
	

'''
# optimized solution
def search_insert(nums,target):
	n = len(nums)
	left,right = 0,n-1
	first_true_index = -1

	while left <= right:
		mid = (left + right) // 2
		if nums[mid] >= target:
			first_true_index = mid
			right = mid -1
		else:
			left = mid + 1

	return first_true_index if first_true_index != -1 else n
'''
print(search_insert(nums,target))