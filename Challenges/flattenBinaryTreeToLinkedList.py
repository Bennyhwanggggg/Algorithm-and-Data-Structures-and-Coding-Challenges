"""
Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Two pass
Time: O(N)
Space: O(N)
"""
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        queue = collections.deque()
        
        def preorder(node):
            if not node:
                return
            queue.append(node)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        
        if not len(queue):
            return
        
        head = queue.popleft()
        while queue:
            head.right = queue.popleft()
            head.left = None
            head = head.right
            

