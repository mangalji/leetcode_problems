# s = "babad"
# s = "bb"
# output = "bab"
# "aba" is also an valid answer
# print(s[::-1])
s = "cbbd"
# output = "bb"

# def checkpal(str,low,high):
# 	while low<high:
# 		if str[low] != str[high]:
# 			return False
# 		low += 1
# 		high -= 1
# 	return True

# def getlongestpal(s):
# 	n = len(s)
# 	maxlen = 1
# 	start_position = 0

# 	for i in range(n):
# 		for j in range(i,n):
# 			if checkpal(s,i,j) and (j-i+1)>maxlen:
# 				start_position = 1
# 				maxlen = j-i+1
# 	return s[start_position:start_position+maxlen]

# print(getlongestpal(s))


def longestPalindrome(s):

	n = len(s)

	dp = [[True]*n for _ in range(n)]

	start = 0
	maxlen = 1

	for i in range(n-2,-1,-1):
		for j in range(i+1,n):
			dp[i][j] = False

			if s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1]

				if dp[i][j] and maxlen < j-i+1:
					start = i
					maxlen = j-i+1
	return s[start:start + maxlen]

print(longestPalindrome(s))

'''
def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[True]*n for _ in range(n)]
        maxlen = 1
        start_position = 0
        
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                dp[i][j] = False

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                    
                    if dp[i][j] and maxlen < j-i+1:
                        start = i
                        maxlen = j-i+1
        return s[start_position:start_position+maxlen]

'''