"""
Interesting String

Given a string s consisting of digits 0-9 and lowercase English letters a-z.

A string is interesting if you can split it into one or multiple substrings, such that each substring starts with a number and this number represents the number of characters after it. Retrun true if string s is intersting, otherwise false.

Example 1:

Input: "4g12y6hunter"
Output: true
Explanation: We can split it into "4g12y" and "6hunter".
Example 2:

Input: "124gray6hunter"
Output: true
Explanation: We can divide it into "12", "4gray", "6hunter".
Example 3:

Input: "31ba2a"
Output: false
Example 4:

Input: "1a"
Output: true
Example 5:

Input: "0"
Output: true
Example 6:

Input: ""
Output: false
Example 7:

Input: "129aaaaaaaaaaa3zyx"
Output: true
Explanation: "129aaaaaaaaaaa" + "3zyx"
"""

def interestingString(s):
    if s == "":
        return False
    dp = [False] * (len(s)+1)
    dp[-1] = True
    for i in range(len(s)-1, -1, -1):
        num = 0
        k = i
        while k < len(s) and s[k].isdigit():
            num = num * 10 + int(s[k])
            if k+num+1 < len(s)+1 and dp[k+num+1]:
                dp[i] = True
                break
            k += 1
    return dp[0]

if __name__ == '__main__':
		assert interestingString("4g12y6hunter") == True
		assert interestingString("124gray6hunter") == True
		assert interestingString("31ba2a") == False
		assert interestingString("1a") == True
		assert interestingString("0") == True
		assert interestingString("") == False
		assert interestingString("129aaaaaaaaaaa3zyx") == True


