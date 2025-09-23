# nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
# unique_val = set(nums)

# nums_list = list(unique_val)

# remain_spot = len(nums)-len(unique_val)

# for i in range(remain_spot):
#     # import ipdb; ipdb.set_trace() 
#     nums_list.append('_')

# return len(unique_val)
# # return nums_list
# # print(nums_list)
# print(nums)
# unique_val = set(nums)
# nums_list = list(unique_val)
# remain_spot = len(nums)-len(unique_val)
# for i in range(remain_spot): 
#     nums_list.append('_')
# print(nums_list)
# nums = nums_list
# print(nums)
# unique_val_list = list(unique_val)
# print(type(unique_val_list))
# # print(unique_val)
# print(unique_val_list)
# print(len(unique_val))



# nums = [1,2,1]
# print(nums)
# # sorted_set = set()
# def remove(nums):
#     sorted_nums = sorted(nums)
#     print(sorted_nums)
#     unique_nums = set(sorted_nums)
#     # print(unique_nums)
#     unique_nums_lst = list(unique_nums)
#     print(unique_nums_lst)
#     remain_spot = len(nums) - len(unique_nums_lst)
#     for i in range(remain_spot):
#         unique_nums_lst.append('_')
#     nums = unique_nums_lst
#     print(nums)
#     return len(unique_nums_lst)

# remove(nums)


# nums = [1,2,1]
# # print(nums)
# nums = sorted(nums)
# unique_nums = set(nums)
# # print(unique_nums)
# # print(unique_nums)
# nums_lst = list(unique_nums)
# # print(nums_lst)

# remain = len(nums) - len(nums_lst)
# # print(remain)
# for i in range(1,remain+1):
#     nums_lst.append('_')
#     # print(i)
# # print(nums_lst)
# nums = nums_lst
# # print(nums)
# length = 0
# for k in nums:
#     if isinstance(k,int):
#         length = length+1
# print(length)
# print(len(unique_nums)) 
# print(len(unique_nums))

# nums = [1,1,2]
# sorted_nums = sorted(nums)
# unique_nums = set(sorted_nums)
# nums_lst = list(unique_nums)
# remain = len(nums) - len(nums_lst)
# for i in range(remain):
#     nums_lst.append('_')
# nums = nums_lst
# length = 0
# for k in nums:
#     if isinstance(k,int):
#         length += 1
# return length


nums = [1,1,2]

unique_nums = set(nums)
unique_nums_list = list(unique_nums)
nums.clear()
nums.extend(unique_nums_list)
return len(nums)
# print(nums)


















