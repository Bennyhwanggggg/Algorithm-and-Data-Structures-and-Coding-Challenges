def highest_product_of_three(nums):
	nums.sort()
	res = 1
	for i in range(3):
		res *= nums.pop()
	return res


def highest_product_of_three_On(nums):
	i, j, k = 0, 1, 2
	maxp = nums[i]*nums[j]*nums[k]
	while i < len(nums) and j < len(nums) and k < len(nums):
		maxp = max(maxp, nums[i]*nums[j]*nums[k])
		current_min = min([nums[i],nums[j],nums[k]])
		if nums[i] == current_min:
			print('2')
			i = max(i, j, k)+1
		elif nums[j] == current_min:
			print('1')
			j = max(i, j, k)+1
		elif nums[k] == current_min:
			k = max(i, j, k)+1
		
	return maxp

def highest_product_of_three_On2(nums):
	if len(nums) < 3:
		return
	highest = max(nums[0], nums[1])
	lowest = min(nums[0], nums[1])
	maxp2 = nums[0] * nums[1]
	lowp2 = nums[0] * nums[1]

	maxp3 = nums[0]*nums[1]*nums[2]

	for i in nums[2:]:
		maxp3 = max(maxp3, maxp2*i, lowp2*i)
		maxp2 = max(maxp2, i*highest, i*lowest)
		lowp2 = min(lowp2, i*highest, i*lowest)
		highest = max(highest, i)
		lowest = min(lowest, i)

	return maxp3


nums = [10, 2, 44, 15, 5, 6, 1, 6, 13, 12, 19, 11, 20, 2, 11, 1, 3, 4, 11, 55]
print(highest_product_of_three_On(nums))
print(highest_product_of_three_On2(nums))
nums = [10, 2, 44, 15, 5, 6, 1, 6, 13, 12, 19, 11, 20, 2, 11, 1, 3, 4, 11, 55]
print(highest_product_of_three(nums))



