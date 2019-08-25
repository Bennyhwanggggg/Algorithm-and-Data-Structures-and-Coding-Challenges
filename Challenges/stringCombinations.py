"""
Given a string s consisting of 0, 1 and ?. The question mark can be either 0 or 1. Find all possible combinations for the string.

Example 1:

Input: s = "001?"
Output: ["0010", "0011"]
"""

def get_string_combinations(s):
	res = []

	def get_strings(s, res, idx):
		if idx == len(s):
			res.append(s)
			return
		if idx < len(s) and s[idx] == '?':
			get_strings(s[:idx] + '0' + s[idx+1:], res, idx+1)
			get_strings(s[:idx] + '1' + s[idx+1:], res, idx+1)
		else:
			get_strings(s, res, idx+1)

	get_strings(s, res, 0)
	return res

if __name__ == '__main__':
	assert get_string_combinations('001?') == ["0010", "0011"]