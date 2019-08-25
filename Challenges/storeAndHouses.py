"""
You are given 2 arrays representing integer locations of stores and houses (each location in this problem is one-dementional). For each house, find the store closest to it.
Return an integer array result where result[i] should denote the location of the store closest to the i-th house. If many stores are equidistant from a particular house, choose the store with the smallest numerical location. Note that there may be multiple stores and houses at the same location.

Example 1:

Input: houses = [5, 10, 17], stores = [1, 5, 20, 11, 16]
Output: [5, 11, 16]
Explanation: 
The closest store to the house at location 5 is the store at the same location.
The closest store to the house at location 10 is the store at the location 11.
The closest store to the house at location 17 is the store at the location 16.
Example 2:

Input: houses = [2, 4, 2], stores = [5, 1, 2, 3]
Output: [2, 3, 2]
Example 3:

Input: houses = [4, 8, 1, 1], stores = [5, 3, 1, 2, 6]
Output: [3, 6, 1, 1]
"""
import bisect

def store_and_houses(houses, stores):
	stores.sort()
	res = []
	for house in houses:
		left, right = 0, len(stores)-1
		ans = -1
		while True:
			mid = (left + right) // 2
			if stores[mid] == house:
				ans = stores[mid]
				break
			if right - left <= 1 :
				break
			elif stores[mid] < house:
				left = mid 
			else:
				right = mid 

		## bisect ver
		# idx = bisect.bisect_left(stores, house)
		# if idx == 0:
		# 	res.append(stores[idx])
		# elif idx == len(stores):
		# 	res.append(stores[idx-1])
		# else:
		# 	ans = stores[idx-1] if abs(house - stores[idx-1]) <= abs(house - stores[idx]) else stores[idx]
		# 	res.append(ans)

		if ans != -1:
			res.append(ans)
			continue
		ans = stores[left] if abs(house - stores[left]) <= abs(house - stores[right]) else stores[right]
		res.append(ans)

	return res

if __name__ == '__main__':
	assert store_and_houses([2, 4, 2], [5, 1, 2, 3]) == [2, 3, 2]
	assert store_and_houses([4, 8, 1, 1], [5, 3, 1, 2, 6]) == [3, 6, 1, 1]
