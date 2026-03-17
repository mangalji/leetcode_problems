#height = [1,8,6,2,5,4,8,3,7]
height = [1,2]
n = len(height)
i = 0
j = n - 1
# ans = max(height)
ans = 0
while i < j:
	val = min(height[i],height[j])
	ans = max((j-i)*val,ans)
	if height[i] < height[j]:
		i += 1
	else:
		j -= 1
print(ans)
