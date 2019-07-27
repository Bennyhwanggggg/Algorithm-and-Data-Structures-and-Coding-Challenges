"""
Given an array of numbers find all the numbers that can be generated from it using +-/() any where between the numbers.
Array can have positive, negative, and duplicate
"""

def findAllNumbers(nums):

	def dfs(nums, res):
		if len(nums) == 1:
			res.add(nums[0])
			return

		for i in range(len(nums)):
			for j in range(len(nums)):
				if i == j:
					continue
				n1, n2 = nums[i], nums[j]
				temp = [nums[k] for k in range(len(nums)) if k != i and k != j]
				temp.append(n1 + n2)
				dfs(temp, res)
				temp.pop()
				temp.append(n1 - n2)
				dfs(temp, res)
				temp.pop()

				if n2 != 0:
					temp.append(n1//n2)
					dfs(temp, res)
					temp.pop()


	res = set()
	dfs(nums, res)
	return res

if __name__ == '__main__':
	assert findAllNumbers([1, 1, 1]) == {0, 1, 2, 3, -1}
	assert findAllNumbers([1, 2, 1]) == {-1, -2, 0, 1, 2, 3, 4}