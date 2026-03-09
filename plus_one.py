# 66. Plus One

# digits = [1,2,3]
# output = [1,2,4]

# digits = [4,3,2,1]
# output = [4,3,2,2]

# digits = [9]
# output = [1,0]

s = ''
for i in digits:
	s += str(i)

s = int(s)
plus_one = s + 1
plus_one_str = str(plus_one)
plus_one_list = []
for j in plus_one_str:
	plus_one_list.append(int(j))

print(plus_one_list)