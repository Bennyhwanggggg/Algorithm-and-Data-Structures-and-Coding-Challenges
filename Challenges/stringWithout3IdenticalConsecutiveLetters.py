"""
Given a string S consisting of N letters a and b. In one move you can replace one letter by the other (a by b or b by a).

Write a function solution that given such a string S, returns the minimum number of moves required to obtain a string containing no instances of three identical consecutive letters.

Example 1:

Input: "baaaaa"
Output: 1
Explanation: The string without three identical consecutive letters which can be obtained is one move is "baabaa".
Example 2:

Input: "baaabbaabbba"
Output: 2
Explanation: There are four valid strings obtainable in two moves, for example "bbaabbaabbaa".
Example 3:

Input: "baabab"
Ouput: 0
Assumptions:

N is an integer within the range [0, ..200,000];
string S consists of only characteres a and b.
"""

def solution(string):
	i = 0
	moves = 0
	while i < len(string):
		run_length = 1
		while i + 1 < len(string) and string[i] == string[i+1]:
			i += 1
			run_length += 1
		moves += run_length // 3
		i += 1

	return moves

if __name__ == '__main__':
	assert solution('baaaaa') == 1
	assert solution('baaaaaa') == 2
	assert solution('baaaab') == 1
	assert solution('baaabbaabbba') == 2
	assert solution('baabab') == 0
	assert solution('bbaabbaabbabab') == 0