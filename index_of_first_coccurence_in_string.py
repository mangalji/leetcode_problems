"""
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
premium lock icon
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""
haystack = "sadbutsad" 
needle = "sad"

index = haystack.find(needle)
# print(index)
if not index and index != 0:
	# print(-1)
	return -1
else:
	# print(index)
	return index

# if index == 0:
# 	print(0)
# 	# return 0
# else:
# 	print(-1)
# 	# return -1