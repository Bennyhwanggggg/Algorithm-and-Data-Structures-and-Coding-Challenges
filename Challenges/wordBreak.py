"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

"""
Brute force using recursion and backtracking. Check every possible prefix of the string and if found, recusively call for the remaining portion of the string.
Time: O(n^n) worse case where every prefix of s is present in the dictionary of words then the recursion tree can grow upto n^n
Space: O(n) depth of recursion
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        res = []
        def backtrack(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in wordDict and backtrack(s, wordDict, end):
                    return True
            return False

        return backtrack(s, set(wordDict), 0)


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


"""
Dynamic Programming bottom up:

We first convert wordDict to a hashset wordSet to facilitate O(1) look-up. Next, we initialize an array of length len(s)+1, where dp[i] denotes if s[:i] can be segmented into words in wordSet. We let dp[0] = 1, because the empty string can be segmented into words in wordSet (trivially). We iterate i over range(1, len(s)+1), and try to find the value for dp[i]. Now dp[i] = 1 if there is some 0 <= j < i, such that dp[j] == 1 and s[j:i] is in wordSet. Therefore, we iterate j in range(i), and check if such a j exists. If it does, we let dp[i] = 1, Otherwise, we let dp[i] = 0. Finally, we return dp[-1] == 1.

Time complexity: O(n**3), where n = len(s), because there are two nested for loops, and the slicing s[j:i] costs an extra O(n). Space complexity: O(n).
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in wordSet:
                    dp[i] = 1
                    break
            else:
                dp[i] = 0
        return dp[-1] == 1

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        def dfs(i):
            if i == len(s):
                return True
            if rec[i] != -1:
                return True if rec[i] == 1 else False
            for j in range(i, len(s)):
                if s[i:j+1] in wordSet:
                    rec[j+1] = 1 if dfs(j+1) else 0
                    if rec[j+1] == 1:
                        return True
            return False
        
        rec = [-1]*(len(s)+1)
        wordSet = set(wordDict)
        return dfs(0)


"""
BFS
Time: O(n^2) ?  For every starting index, the search can continue till the end of the given string.
Space: O(n)
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        queue = [0]
        slen = len(s)
        lenList = [l for l in set(map(len,wordDict))]
        visited = [0 for _ in range(0, slen + 1)]
        while queue:
            tmpqueue = []
            for start in queue:
                for l in lenList:
                    if s[start:start+l] in wordDict:
                        if start + l == slen:
                            return True
                        if visited[start + l] == 0:
                            tmpqueue.append(start+l)
                            visited[start + l] = 1
            queue, tmpqueue = tmpqueue, []
        return False

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        queue = [0]
        ls = len(s)
        lenList = [l for l in set(map(len, wordDict))]
        visited = [0 for _ in range(0, ls + 1)]
        while queue:
            start = queue.pop(0)
            for l in lenList:
                if s[start:start + l] in wordDict:
                    if start + l == ls:
                        return True
                    if visited[start + l] == 0:
                        queue.append(start + l)
                        visited[start + l] = 1
        return False


"""
Use word mapping but memeroy exceed so use the other bfs
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = collections.defaultdict(list)
        for word in wordDict:
            words[word[0]].append(word)
        
        queue = collections.deque([(x, '') for x in words[s[0]]])
        while queue:
            word, currString = queue.popleft()
            currString += word
            if currString == s:
                return True
            if len(currString) >= len(s):
                continue
            currIdx = len(currString)
            currChr = s[currIdx]
            for nextWord in words[currChr]:
                queue.append((nextWord, currString))
        return False

"""
DFS with cache
"""
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        memo = {}
        def DFS(s):
            if not s:
                return True
            if s not in memo:
                memo[s] = False
                for i in range(1,len(s)+1):
                    if s[:i] in wordDict:
                        if DFS(s[i:]):
                            memo[s] = True
                            break
                return memo[s]
        return DFS(s)  

"""
Second solution: DP
dp[i] is set to true if a valid word (word sequence) ends there.
The optimization is to look from current position i back .
if s[j:i] in wordDict and dp[j] == true , dp[i] == true .
"""
# dp
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        for i in range(1,len(s)+1):
            for w in wordDict:
                if (i-len(w)) > -1:
                    if s[i-len(w):i] == w and (i-len(w) == 0 or dp[i-len(w)]):
                        dp[i] = True
                        break
        return dp[-1]
