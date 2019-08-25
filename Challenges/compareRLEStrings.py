"""
Given 2 run-length encoded strings s and t. Determine if they represent the same string.

Example 1:

Input: s = "3a1b", t = "2a1a1b"
Ouptut: true
Example 2:

Input: s = "3a1b3c", t = "2a1a1b2c1d"
Ouptut: false
Expected O(1) space solution.

Follow-up:
Given a RLE string s and a width of a board. Assume that the board is filled from left to right such that each line has exactly width chars. Output the RLE string that represents the board rows from right to left without constructing the board.

Example:

Input: s = "3a1b3c3d2a", width = 4

aaab
cccd
ddaa

Output: "1b3a1d3c2a2d"
"""

def compareRLE(s, t):

	def build(s):
		res = ''
		i = 0
		while i < len(s):
			n = 0
			if s[i].isdigit() and int(s[i]) == 0:
				i += 2
				continue
			while i < len(s) and s[i].isdigit():
				n = n*10 + int(s[i])
				i += 1
			res += s[i] * n
			i += 1
		return res

	s_expand = build(s)
	t_expand = build(t)
	return s_expand == t_expand

if __name__ == '__main__':
	assert compareRLE('3a1b', '2a1a1b') == True
	assert compareRLE('3a1b3c', '2a1a1b2c1d') == False
	assert compareRLE('3a0b', '2a1a') == True

