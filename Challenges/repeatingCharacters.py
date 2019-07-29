"""
Twitch Words

You are given a word like hellloooo print all the repeating character index and the number of time it is has been repeated.

Example 1:

Input: "hellloooo"
Output: [[2, 3], [5, 4]]
Explanation: hellloooo has l and o as repeating characters so return index of l which is at 2
and the number of times it has been repeated is 3. Same goes for O.
Example 2:

Input: "leetcodeee"
Output: [[1, 2], [7, 3]]
Follow-up:
What if you need to print the repeated character as well?

Example 1:

Input: "hellloooo"
Output : [['l', 3], ['o', 4]]
Example 2:

Input: "leetcodeee"
Output: [['e', 5]]
"""

"""
Time: O(N)
Space: O(1)
"""
def repeatingCharacters(s):
	res = []
	index, count = -1, 1
	for i in range(1, len(s)+1):
		if len(s) == i or (count > 1 and s[i-1] != s[i]):
			res.append([index, count])
			index = -1
			count = 1
		elif s[i-1] == s[i]:
			count += 1
			if index < 0:
				index = i-1
	return res

if __name__ == '__main__':
	assert repeatingCharacters('hellloooo') == [[2, 3], [5, 4]]
	assert repeatingCharacters('leetcodeee') == [[1, 2], [7, 3]]
