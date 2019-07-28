"""
Given an array -> [2,3,1,4,9]. You can choose either element from beginning or end of the array. 
Keep choosing until you've chosen N/2 elements( where N is array size ).

Find the maximum sum of N/2 elements chosen this way.
"""

"""
For those who don't get it first hand like me, here's a brief explanation:
It's basically a complement sliding window implementation where the desired values start getting considered once we reach the halfway mark.

For the example [2,3,5,4,9,1] we have the following combinations sum possible
2+3+5 (first 3)
4+9+1 (last 3)
2+3+1 (take the first two from the front and one from the back)
1+2+3 (take one from the back and two from the front -- Notice this is exactly the same as the last one because we're dealing with combinations not permutations so we can ignore this repeated combo)
2+1+9 or 1+9+2 (1 from the front and 2 from the back)
So overall there are only 4 possibilities or N/2 + 1 where N is the size of nums.

Now you can notice a pattern (kinda hard to see at first) that ALL of these numbers that we want (2+3+5, 2+9+1, 2+3+1, 4+9+1) are all just complements of a sliding window once we get to the halfway point. Here's how to visualize it

2 3 4 5 9 1 
^ ^ ^
complement of 2 + 3 + 4 is total - the sum of the ^'s = 5+9+1 (the ones not selected with ^'s)
2 3 4 5 9 1
    ^ ^   ^  
complement of 3+ 4 + 5 = Total - the sum of the ^'s  = 2 + 9 + 1

Now you're seeing a pattern? Let's do one more
2 3 4 5 9 1
       ^ ^  ^  
complement of 4+5+9 = 2+3+1

So you realize that every single combination we desire or want to generate doesn't have to be generated recursively using stack space but just in o(n)! That's the genius of it (at least I find it genius), so all we have to do is max all these complements (or alternatively min all the sums then find the complement of that min i.e. total - min)
"""
def maxSum(arr):
	n = len(arr)
	if n%2:
		k = n-(n//2)-1
	else:
		k = n-(n//2)
	smallest = float('inf')
	total, curr = 0, 0
	for i in range(n):
		curr += arr[i]
		total += arr[i] 
		if i > k:
			curr -= arr[i-k]
		if i >= k-1:
			smallest = min(smallest, curr)
	print(total-smallest)
	return total - smallest

if __name__ == '__main__':
	assert maxSum([2, 3, 1, 4, 9]) == 14
	assert maxSum([2, 3, 1, 2, 4, 9]) == 15

