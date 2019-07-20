# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            result.append([node.val for node in queue])
            queue = [q for node in queue for q in (node.left, node.right) if q]
        result.reverse()
        return result
            
class Solution:
    def levelOrderBottom(self, root):
        # not allowed to reverse the list
        result = []
        if root == None:
            return result
        
        def bfsbottomup(result, prev):
            if prev == []:
                return
            temp = []
            cur = []
            for node in prev:
                temp.append(node.val)
                if node.left != None:
                    cur.append(node.left)
                if node.right != None:
                    cur.append(node.right)
            bfsbottomup(result, cur)
            result.append(temp)
            
        bfsbottomup(result, [root])
        return result

