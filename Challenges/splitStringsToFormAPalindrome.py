"""
Given 2 strings a and b with the same length. Strings are alligned one under the other. We can choose an index and split both strings into 4 subtrings: a1 + a2 and b1 + b2. Find out if it's possible to split a and b such that a1 + b2 or a2 + b1 forms a palindrome.

Example 1:

Input: a = "abcbbbb", b = "xxxbcba"
Output: true
Explanation: 

abc|bbbb
xxx|bcba

We can split the strings at index 3. We will get a1 = "abc", a2 = "bbbb" and b1 = "xxx", b2 = "bcba"
a1 + b2 forms a palidnrome "abcbcba" so return true.

Follow-up:
Now it's allowed to split the strings independently:

a|bcbbbb
xxxbcb|a
So in the exampe above a can be splitted into a1 = "a" a2 = "bcbbbb" and b can be splitted b1 = "xxxbcb" b2 = "a". As a result a1+ b2 forms a palindrome "aa". Find the longest palindrome.


The follow-up, in O(N): example abcbbbb, xxxbcba

Get via two pointers the longest a1,b2, where a1 and b2 are same size and a1+b2 == palindrome. (abcb+bcba)
Now the remaining a2+b1 is NOT a palindrome, so we have to make the the a cut there or b cut there. (bbb & xxx)
Now this means you're interested in the longest palindrome substring of a2 starting at its beginning (in case we did the b cut), or longest palindrome substring of b1 ending at its end (in case we did the a cut), which can be solved via KMP in O(N), see here - https://leetcode.com/problems/shortest-palindrome/ (both bbb and xxx are valid such, so answer is either abcb+bbb+bcba or abcb+xxx+bcba)
"""

"""
Two pointers, once you find an unmatch, check if added by remain gives a palindrome
The important intuition is that the center of the split palindrome string has to be the same as the center of the input strings.
"""
def splitStringToFormPalindrome(A, B):
	i, j = 0, len(A)-1
	while i <= j:
		if A[i] == B[j]:
			i += 1
			j -= 1
		else:
			return A[i:j+1] == A[i:j+1][::-1] or B[i:j+1] == B[i:j+1][::-1]
	return True

def check(A, B):
	return splitStringToFormPalindrome(A, B) or splitStringToFormPalindrome(B, A)

if __name__ == '__main__':
	assert check('abcgggg', 'xxxbcba') == True
	assert check('adbbbb', 'xxbcba') == False
	assert check('abcxxcagxxxx', 'xxxddddddcba') == True
	assert check('abcxxcagxxx', 'xxxdddddcba') == True
	assert check('ABCXYZXX', 'XYZYXCBA') == True
	assert check('abfjkdk', 'xycdcba') == True
	assert check('xycdcba', 'abfjkdk') == True
	assert check('xbxtba', 'abtacx') == True

	