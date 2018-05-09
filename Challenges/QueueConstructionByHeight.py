class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0:
            return []
        n = len(people)
        res = []
        people.sort(key=lambda x:(x[0], -x[1]), reverse=True)
        for p in people:
            res.insert(p[1], p)
        return res