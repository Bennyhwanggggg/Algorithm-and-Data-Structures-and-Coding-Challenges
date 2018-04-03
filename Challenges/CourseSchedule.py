class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        res = numCourses
        indegrees = [0] * numCourses
        for edge in prerequisites:
            curr, prereq = edge
            indegrees[curr] += 1

        q = collections.deque()
        for i in range(len(indegrees)):
            if not indegrees[i]:
                q.append(i)

        while q:
            pre = q.popleft()
            res -= 1
            for edge in prerequisites:
                curr, prereq = edge
                if prereq == pre:
                    indegrees[curr] -= 1
                    if not indegrees[curr]:
                        q.append(curr)

        return res == 0

