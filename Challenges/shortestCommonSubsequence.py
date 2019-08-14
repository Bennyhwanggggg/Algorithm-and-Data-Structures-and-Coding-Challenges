"""
Shortest Common Supersequence

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.  If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T (possibly 0, and the characters are chosen anywhere from T) results in the string S.)

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
 

Note:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
"""

"""
Thought process
dp(i, j) represents the shortest supersequence for str1[i:] and str2[j:]

transition function

if str1[i] == str2[j], simply return str1[i] + dp(i+1, j+1)
if str1[i] != str2[j]:
there are two options:
add an extra str2[j] at the beginning, then try to find the supersequence for str1[i:] and str2[j+1:]
try to find the first index of str2[j] in str1[i:]
if such index exists, the candidate supersequence is str1[i:index+1] + dp(index+1, j+1)
otherwise, the candidate supersequence is str1[i:] + str2[j:]
return the candidate supersequence with minimum length
base case:

i >= m or j >= n: return the other string
time complexity: O(mn), where m is the length of str1, and n is the length of str2

space complexity: O(mn)
"""
def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        @functools.lru_cache(None)
        def dp(i, j):
            if i >= m:
                return str2[j:]
            if j >= n:
                return str1[i:]
            if str1[i] != str2[j]:
                cand1 = str2[j] + dp(i, j+1)
                index = str1.find(str2[j], i+1)
                if index == -1:
                    cand2 = str1[i:] + str2[j:]
                else:
                    cand2 = str1[i:index+1] + dp(index+1, j+1)
                return cand1 if len(cand1) < len(cand2) else cand2
            else:
                return str1[i] + dp(i+1, j+1)
        return dp(0, 0)


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [str1[:i] for i in range(len(str1)+1)]
        for i in range(1,len(str2)+1):
            new = [str2[:i]]
            for j in range(1,len(dp)):
                if str1[j-1] == str2[i-1]:
                    new += [dp[j-1] + str1[j-1]]
                else:
                    t1 = new[j-1] + str1[j-1]
                    t2 = dp[j] + str2[i-1]
                    if len(t1) < len(t2):
                        new += [t1]
                    else:
                        new += [t2]
            dp = new
        return dp[-1]

