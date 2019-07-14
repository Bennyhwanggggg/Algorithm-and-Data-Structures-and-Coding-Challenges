"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

"""
Time: O(n^2) inserting each person into the result list
Space: O(n) to store result

People are only counting (in their k-value) taller or equal-height others standing in front of them. So a smallest person is completely irrelevant for all taller ones. And of all smallest people, the one standing most in the back is even completely irrelevant for everybody else. Nobody is counting that person. So we can first arrange everybody else, ignoring that one person. And then just insert that person appropriately. Now note that while this person is irrelevant for everybody else, everybody else is relevant for this person - this person counts exactly everybody in front of them. So their count-value tells you exactly the index they must be standing.

So you can first solve the sub-problem with all but that one person and then just insert that person appropriately. And you can solve that sub-problem the same way, first solving the sub-sub-problem with all but the last-smallest person of the subproblem. And so on. The base case is when you have the sub-...-sub-problem of zero people. You're then inserting the people in the reverse order, i.e., that overall last-smallest person in the very end and thus the first-tallest person in the very beginning. That's what the above solution does, Sorting the people from the first-tallest to the last-smallest, and inserting them one by one as appropriate.
"""
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

	# this sorts the list by height where the largest heights are first. 
        # each group of heights is also sorted in ascending order
        # (e.g. [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]] would be the
        # resulting list after sorting the default test case for run code)
        people.sort(key=lambda x:(x[0], -x[1]), reverse=True)


	# by inserting each person into the new list using k as the insertion
        # index and by starting with the tallest people we leverage the what 
        # insertion does: push every element behind it back 1. By inserting 
        # from tallest to shortest, we make sure that, at the time of insertion,
        # everything is being put into the list with exactly k people in front
        # of them that are taller or equal in height
        for p in people:
            res.insert(p[1], p)
        return res
