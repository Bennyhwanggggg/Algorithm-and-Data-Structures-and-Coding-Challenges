"""
Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Same as the preorder and inorder one but reverse
Notice inorder traversal's property where it's idx is indication of right or left subtree
Time: O(N)
Space: O(N)
"""
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        postorder.reverse()
        
        idx = {val: i for i, val in enumerate(inorder)}
        
        stack = []
        head = None
        for val in postorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] > idx[stack[-1].val]:
                    stack[-1].right = node
                else:
                    while stack and idx[val] < idx[stack[-1].val]:
                        u = stack.pop()
                    u.left = node
                stack.append(node)
        return head

