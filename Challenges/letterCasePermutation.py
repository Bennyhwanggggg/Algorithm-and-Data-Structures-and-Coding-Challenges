"""
Letter Case Permutation

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
"""

"""
Time: O(2^N * N) We generate 2^N and test N times
Space: O(2N *N)
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        
        def dfs(s, curr):
            if not len(s) or s.isdigit():
                ans = ''.join(curr) + s
                if len(ans) == len(S):
                    self.res.append(ans)
            
            for i in range(len(s)):
                if s[i].isdigit():
                    curr += [s[i]]
                    continue
                dfs(s[i+1:], curr+[s[i].lower()])
                dfs(s[i+1:], curr+[s[i].upper()])
        
        dfs(S, [])
        return self.res
    
## Blog link: https://brain.dennyzhang.com/letter-case-permutation
class Solution:
    ## Basic Ideas: One pass (similar like DFS)
    ##
    ## Complexity: Time O(n*pow(2,n)), Space O(pow(2, n))
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for ch in S:
            l = []
            for item in res:
                if ch.isdigit():
                    l.append("%s%s" % (item, ch))
                else:
                    l.append("%s%s" % (item, ch.lower()))
                    l.append("%s%s" % (item, ch.upper()))
            res = l
        return res
        
    ## Basic Ideas: BFS
    ##
    ## Complexity: Time O(n*pow(2, n)), Space O(pow(2, n))
    def letterCasePermutation_v1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)
        if length == 0: return [""]
        import collections
        queue = collections.deque()
        queue.append("")
        level = -1
        while True:
            level += 1
            if level == length: break
            for k in range(len(queue)):
                ch = S[level]
                element = queue.popleft()
                if ch.isdigit():
                    queue.append("%s%s" % (element, ch))
                else:
                    queue.append("%s%s" % (element, ch.lower()))
                    queue.append("%s%s" % (element, ch.upper()))
        return list(queue)
            
    ## Basic Ideas: recursive
    ##
    ## Complexity: Time O(n*pow(2, n)), Space O(pow(2, n))
    def letterCasePermutation_v1(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)
        if length == 0: return [""]
        res = []
        ch = S[0]
        for item in self.letterCasePermutation(S[1:]):
            if ch.isdigit():
                res.append("%s%s" % (ch, item))
            else:
                res.append("%s%s" % (ch.lower(), item))
                res.append("%s%s" % (ch.upper(), item))
        return res

