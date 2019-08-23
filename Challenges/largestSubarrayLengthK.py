"""
Largest Subarray Length K

Array X is greater than array Y if the first non matching element in both 
arrays has a greater value in X than Y.

For example:
X = [1, 2, 4, 3, 5]
Y = [1, 2, 3, 4, 5]

X is greater than Y because the first element that does not match is larger in X.
and if
A = [1, 4, 3, 2, 5] and  K = 4, the result is 
[4, 3, 2, 5]
"""

# my interpretation is that we can look at all the possible starting indices for a starting array and compare the first value. All elements are unique (distinct), so one value within an array will always be larger or smaller than another--giving us the largest subarray if we just compare that first index.

# if A is all unique
"""
Time: O(N), space: O(1)
"""
def solution(a, k):
	# store the first starting index for a subarray as the largest since len(a) will be <= k
	first_idx = 0

	for x in range(1, len(a)-k+1):  # check indices where a subarray of size k can be made
		# replace the largest first index if a larger value is found
		first_idx = x if a[first_idx] < a[x] else first_idx

	return a[first_idx:first_idx+k]

def solution2(a, k):
  first_idx = 0
  for x in range(1, len(a) - k + 1):
    # compare values at each index for the would be sub arrays
    for i in range(k):
      # replace the largest index and break out of the inner loop is larger value is found
      if a[first_idx + i] <= a[x + i]:
        first_idx = x
        break
      # if the current stored largest subarray is larger than the current subarray, move on
      else:
        break

  return a[first_idx:first_idx+k]

if __name__ == '__main__':
	assert solution(a=[1, 4, 3, 2, 5], k=4) == [4, 3, 2, 5]
	assert solution2(a=[1, 4, 3, 2, 5], k=4) == [4, 3, 2, 5]
	assert solution2(a=[1, 4, 4, 2, 5], k=4) == [4, 4, 2, 5]


