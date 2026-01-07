'''Leetcode problem name = Majority element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

 
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''


# Normal/Simple/Easy solution (time taking when run)

# nums = [1,1,1,1,1,1,8]
# def maj(nums):
# 	maj_ele = {}
# 	for num in nums:
# 		num_ele = num
# 		occurs = nums.count(num)
# 		maj_ele[num_ele] = occurs
# 	# print(maj_ele)
# 	for key,value in maj_ele.items():
# 		if value > len(nums)/2:
# 			# print(key)
# 			return key

# print(maj(nums))


# optimized solution

from collections import defaultdict

nums = [1,1,1,1,1,1,8]
def maj(nums):
    n = len(nums)
    
    count = defaultdict(int)
    
    for num in nums:
        count[num] += 1
        if count[num] > n // 2:
            return num
            # print(num)
    return -1

print(maj(nums))
