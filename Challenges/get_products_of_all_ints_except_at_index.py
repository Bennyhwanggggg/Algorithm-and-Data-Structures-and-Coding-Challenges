def get_products_of_all_ints_except_at_index(nums):
	result = []
	for i in range(len(nums)):
		product = 1
		for j in range(len(nums)):
			if i != j:
				product *= nums[j]
		result.append(product)
	return result


def get_products_of_all_ints_except_at_index2(nums):
	p = 1
	result = [None] * len(nums)
	for i in range(len(nums)):
		result[i] = p
		p *= nums[i]
	p = 1
	for j in range(len(nums)-1, -1, -1):
		result[j] *= p
		p *= nums[j]

	return result


print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
print(get_products_of_all_ints_except_at_index2([1, 7, 3, 4]))
