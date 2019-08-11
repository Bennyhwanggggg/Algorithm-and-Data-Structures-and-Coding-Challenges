"""
Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

"""
Course Schedule

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

"""
BFS
Time: O(N+E)
Space: O(N+E)
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = numCourses
        indegrees = [0] * numCourses
        graph = collections.defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1
            
        queue = collections.deque()
        for course in range(numCourses):
            if not indegrees[course]:
                queue.append(course)

        taken = set()
        while queue:
            currCourse = queue.popleft()
            taken.add(currCourse)
            for course in graph[currCourse]:
                indegrees[course] -= 1
                if not indegrees[course]:
                    queue.append(course)

        return res == len(taken)


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

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] = indegree.get(course, 0) + 1
        
        taken = set()
        queue = collections.deque([course for course in range(numCourses) if indegree[course] == 0])
        while queue:
            course = queue.popleft()
            taken.add(course)
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] <= 0:
                    queue.append(nei)
        return len(taken) == numCourses
