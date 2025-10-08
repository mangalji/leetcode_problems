nums = [2,1,5,0,4,6]

# for i in range(len(nums)):
# 	for j in range(i+1,len(nums)):
# 		for k in range(j+1, len(nums)):
# 			if nums[i] < nums[j] < nums[k]:
# 				print(True)
# 				break

for i in range(len(nums)):
    if nums[i] < nums[i+1] < nums[i+2]:
        print(True)
        break
    else:
        print(False)

	# if nums[i] < nums[i+1] and nums[i+1] < nums[i+2]:
	# 	print(True)
	# else:
	# 	print(False)