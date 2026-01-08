'''136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

'''
from collections import defaultdict
nums = [4,1,2,1,2]

n = len(nums)

dct = defaultdict(int)

for num in nums:
	dct[num] += 1
	# if dct[num] <= 1:
	# 	print(dct[num])
for i,j in dct.items():
	if j == 1:
		print(i)

