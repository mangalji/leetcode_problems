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
# # strs = ["dog","racecar","car"]
# string = ''
# s = ''
# t = ''
# for i in range(len(strs)):
# 	# print(strs[i])
# 	a = strs[i]
# 	# print(a)
# 	print('-----')
# 	for j in range(len(a)):
# 		s += a[j]

# 		# print(a[j])
# 		# if a[j] == :
# 		# 	print(True)
# 		# else:
# 		# 	print(False)




strs = ["flower","flow","flight"]
for i in range(len(strs[0])):
 	for string in strs[1:]:
 		if len(string) <= i or string[i] != strs[0][i]:
 			# return strs[0][:i]
 			print(strs[0][:i])

 # return strs[0]
print(strs[0])


# 	for j in range(len(strs[i])+1):
# 		print(strs[i][j])
# 		a = strs[i]
# 		print(a)
# 		a1 = a[j]
# 		print(a1)
# 		b=strs[i+1]
# 		print(b)
# 		b1=b[j]
# 		print(b1)
# 		if a1 == b1:
# 		# if strs[i][j] == strs[i+1][j]:
# 			string += strs[i][j]
# 		else:
# 			continue

# print(string)