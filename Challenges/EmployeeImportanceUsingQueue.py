"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic={}
        for e in employees:
            dic[e.id]=e
        
        substack=collections.deque()
        substack.append(id)
        res=0
        while substack:
            s=substack.popleft()
            if s not in dic:
                return 'error'
            res+=dic[s].importance
            for p in dic[s].subordinates:
                substack.append(p)
        return res
                