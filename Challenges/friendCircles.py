"""
Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""

"""
DFS
Time: O(N^2)
Space: O(N)
"""
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    graph[i].append(j)
        
        count = 0
        for i in range(len(M)):
            stack = graph[i]
            seen = set(stack)
            if stack:
                count += 1
            while stack:
                curr = stack.pop()
                seen.add(curr)
                while graph[curr]:
                    nei = graph[curr].pop()
                    if nei not in seen:
                        stack.append(nei)
        return count
    
"""
Recursive
"""
class Solution:
    def findCircleNum(self, A):
        N = len(A)
        seen = set()
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj == 1 and nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
    
"""
Iterative
"""
class Solution(object):
    def findCircleNum(self, M):
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        for j, v in enumerate(M[cur]):
                            if v == 1 and j not in seen:
                                toSee.append(j)
                res += 1
        return res
                

