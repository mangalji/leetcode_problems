s = "pwwkew"
s = 'bbbbb'
s = 'abcabcbb'
def long_string(s):
	ss = ''
	for i in s:
		if i in ss:
			# return len(ss)
			ss = ''
			continue
		else:
			ss += i
	return len(ss)

print(long_string(s))