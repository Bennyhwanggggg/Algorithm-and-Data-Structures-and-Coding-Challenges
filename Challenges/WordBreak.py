"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
"""

"""
Brute force using recursion and backtracking. Check every possible prefix of the string and if found, recusively call for the remaining portion of the string.
Time: O(n^n) worse case where every prefix of s is present in the dictionary of words then the recursion tree can grow upto n^n
Space: O(n) depth of recursion
"""
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         length = len(s)
#         res = []
#         def backtrack(s, wordDict, start):
#             if start == len(s):
#                 return True
#             for end in range(start+1, len(s)+1):
#                 if s[start:end] in wordDict and backtrack(s, wordDict, end):
#                     return True
#             return False
 
#         return backtrack(s, set(wordDict), 0)


"""
DP solution
Time: O(n^2)
Space: O(n)

Divide into s1 and s2 subproblem and if the subproblems satisfies the condition, then return true. Keep going into smaller subproblems with each index as the end point. 

Two index pointers, i and j where i is the length of the substring currently and j is the split index of the current substring.
Consider all possible length sub string.
"""
class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
                
                

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]
