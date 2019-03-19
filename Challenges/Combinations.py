class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        stack = [(0, [])]
        res = []
        while stack:
            cur, path = stack.pop()
            if len(path) == k:
                res.append(path)    
            if cur < n:
                stack.extend([(i, path+[i]) for i in range(cur+1, n+1) if len(path) < k])
        return res


# recursive
class Solution2(object):
    def getCombine(self, n, k, index, prev, ans):
        if len(prev)==k:
            ans.append(prev)
            return
        for i in range(index,n-(k-len(prev))+2):
            self.getCombine(n, k, i+1, prev+[i], ans)

    def combine(self, n, k):
        ans = []
        if k <= n:
            self.getCombine(n, k, 1, [], ans)
        return ans