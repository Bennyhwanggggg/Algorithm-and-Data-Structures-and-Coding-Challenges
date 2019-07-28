"""
return the lowest palindromic score. For instance, a string input ASAP can have two score 4 or 4/3 becuase 
ASA is palindrom and calculated as 1/3 + "P" is palindrom 1/1 total score 4/3 or 1 for each character. 
The api should return 4/3.
"""

"""
for 2nd, 'a' is a character array representing input string
keep dp[i], representing number of palindromes to represent a[0..i]. initially, its dp[i] = i+1
foreach c in a:
find out possible palindrome with c in the middle (both even and odd possibilities), lets say evenp and oddp are these palindromes.
dp[i+length(evenp)/2] = min( dp[i-length(evenp)/2]+1/length(evenp), dp[i+length(evenp)/2] )
dp[i+length(oddp)/2] = min( dp[i-length(oddp)/2]+1/length(oddp), dp[i] )

return dp[length(a)-1]


for the second problem, I think it is a dp problem, 
dp[i] means that the min score for substring of the string from index 0 to index i-1. 
Before working on dp for loop, we need to use a map to store palindrome substring 's starting index, 
and ending index. Map<Integer, Set> map, the key of map will represent the palindrome substring ending 
index, and the value set of the map represent all of starting indexes of the palindrome substring whose 
ending index is key. Then, the processing map need to take O(N^2) time complexity, and the dp process 
needs to take worst case O(N^2). Thus, I think the total complexity is O(N^2)
"""

# Time: O(N^2) Space: O(N^2)
def lowestPalindromicScore(s):
	n = len(s)
	scores = [0]*n
	dp = [[False for _ in range(n)] for _ in range(n)]

	for i in range(n):
		scores[i] = i+1 # highest score for when each character gives a palindrome
		for j in range(i+1):
			if s[j] == s[i] and (i - j < 2 or dp[j+1][i-1]):
				dp[j][i] = True
				scores[i] = (1.0/(i+1)) if j == 0 else min(scores[i], scores[j-1] + 1.0/(i-j+1))

	return scores[n-1]

def printgrid(grid): # debug stuff
	for row in grid:
		print(row)

if __name__ == '__main__':
	assert lowestPalindromicScore('ASAP') == 4/3