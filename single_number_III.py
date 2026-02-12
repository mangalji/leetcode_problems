from collections import defaultdict
n = [1,2,1,3,2,5]

count = defaultdict(int)
res = []
for num in n:
	count[num] += 1

for i,j in count.items():
	if j == 1:
		res.append(i)

print(res)