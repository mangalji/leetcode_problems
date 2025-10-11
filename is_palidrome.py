"""
Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""

# s = "A man, a plan, a canal: Panama"
s = "race a car"

t = ''

for i in range(len(s)):
	# print(i)
	# print(s[i])
	if s[i].isalnum() == True:
		# print(s[i])
		t += s[i]
	else:
		continue

# print(t)
t = t.lower()
if t == t[::-1]:
	print(True)
else:
	print(False)
# # s = s.lower().replace(' ','')
# print(s)
# print(s[-1::-1])
# if s == s[::-1]:
# 	print(True)
# else:
# 	print(False)