# arr_input = input("enter the array items(by using commaas): ")
# # arr = arr_input.split(",")
# arr = list(map(int,arr_input.split(",")))
# print(arr)
arr = [2,2,1,1,5,3,3,5]
# arr = [1,1,2,2,1]
existed_ele = []
current_frequency = 0
last_frquency = 0
frequency_count = 0

for i in range(len(arr)):
	print("current item: ",arr[i])
	print("+++++++++++++++++++++++++++++++")
	if i == 0:
		existed_ele.append(arr[i])
		print("existed_ele list: ",existed_ele[i])
		current_frequency = 1
		print("current_frequency: ",current_frequency)
		frequency_count = 1
		print("frequency_count: ",frequency_count)
		last_frquency = current_frequency
		print("last_frquency: ",last_frquency)
		print("____________________________________")

	elif i > 0:
		# print("current item: ",arr[i])
		if arr[i] in existed_ele:
			print(f"current item: {arr[i]}, full arr list: {arr}, current existed_ele: {existed_ele}")
			current_frequency = existed_ele.count(arr[i]) + 1
			existed_ele.append(arr[i])
			print("current_frequency: ",current_frequency)
			if current_frequency != last_frquency:
				frequency_count += 1
				print("frequency_count: ",frequency_count)
				last_frquency = current_frequency
				print("last_frquency: ",last_frquency)
			else:
				continue
			print("--------------------------------------------")
		elif arr[i] not in existed_ele:
			print("new item: ",arr[i])
			existed_ele.append(arr[i])
			# last_frquency = current_frequency
			current_frequency = 1
			print("last_frquency: ",last_frquency)
			print("frequency_count(before new frequency): ",frequency_count)
			print("current_frequency: ",current_frequency)
			
			if current_frequency != last_frquency:
				frequency_count += 1
				last_frquency = current_frequency
				print("frequency_count(after new frequency): ",frequency_count)
				print("last_frquency: ",last_frquency)
			else:
				continue
	print(f"=============== {i}th iteration complete ===============")

print(frequency_count)
