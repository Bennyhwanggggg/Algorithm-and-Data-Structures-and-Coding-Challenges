"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
"""

"""
Sliding Window
Keep track of the count of the different elements in the current window and if 
there are more than k items, start deleting from the first pointer until two items
left.
Time: O(n)
Space: O(1) since only k baskets
"""
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not len(tree):
            return 0
        
        count = dict()
        i = 0
        res = 0
        for j, x in enumerate(tree):
            count[x] = count.get(x, 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        counts = dict()
        res = 0
        
        start = 0
        for end in range(len(tree)):
            counts[tree[end]] = counts.get(tree[end], 0) + 1
            while len(counts) > 2 and start < end:
                counts[tree[start]] -= 1
                if counts[tree[start]] == 0:
                    del counts[tree[start]]
                start += 1
            res = max(res, end - start + 1)
        return res
                
