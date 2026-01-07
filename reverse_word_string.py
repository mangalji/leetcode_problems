'''151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.'''


# output = "blue is sky the"

# s = "  hello world  "
# s = "a good   example"

# output = ""

# for i in range(len(s)):

# 	output += s[i]

# 	if s[i] == " " and (s[i+1]) == " ":
# 		continue

# # reverse = output[::-1]
# # return output
# print(reverse)
s = "the  sky is blue"

lst = s.split()
# print(type(lst))
a = []
for i in range(len(lst)-1,-1,-1):
	a.append(lst[i])

reverse = ' '.join(a)
print(reverse)
print(type(reverse))






















