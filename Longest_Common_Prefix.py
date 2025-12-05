"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
strs = ["flower","flow","flight"]

def long(strs):
	common_prefix = ""
	
	for i in range(len(strs[0])):
		for s in strs:
			if i == len(s) or s[i] != strs[0][i]:
			# if strs[0][i] != s[i]:
				return common_prefix
		common_prefix += strs[0][i]
	
	return common_prefix

print(long(strs))