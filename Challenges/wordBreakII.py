"""
Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""

"""
DFS

1.Every time, we check whether s starts with a word. If so, we check whether the substring s[len(word):] starts with a word, etc.
2.resultOfTheRest keeps calling until we hit the last word. If the last word is in the dict, we append it to res.
The last word is 'dog ==> 'res = [ "dog"]
3. This time, we skip "else," since we fulfill the condition " if len(word) == len(s)." We store it in memo: {'dog': ['dog']}

4.Then we return to "resultOfTheRest = self.helper(s[len(word):], wordDict, memo)"
s = "sanddog" because we start with "cat" (cat is the first word in the dict) and "cat" leads to "sand".
resultOfTheRest = ["dog"]
word = "sand"
item = "sand dog"
res = ["sand dog"]
memo ={'dog': ['dog'], "sanddog":["sand dog"] }

Why do we need memo?
We always recurse to the last word in the string and backtrack, so storing all possible combinations of the substring in the memo saves time for the next iteration of the whole string. For example, "catsanddog," if we don't store "dog," then we have to iterate through the dictionary. This is very DP.

Time: O(n^3) size of recursion is n^2 and we go through n results
Space: O(n^3)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def dfs(s, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return []
            res = []
            for word in wordDict:
                if not s.startswith(word):
                    continue
                if len(word) == len(s):
                    res.append(word)
                else:
                    remains = dfs(s[len(word):], wordDict, memo)
                    for remain in remains:
                        remain = '{} {}'.format(word, remain)
                        res.append(remain)
            memo[s] = res
            return memo[s]
        
        memo = dict()
        return dfs(s, wordDict, memo)

