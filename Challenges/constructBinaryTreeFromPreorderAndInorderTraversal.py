"""
Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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

Given a binary tree:

						8                       
            ┌───────────┴───────────┐           
            3                      10           
      ┌─────┴─────┐                 └─────┐     
      1           6                      14     
               ┌──┴──┐                 ┌──┘     
               4     7                13
So, its pre-order traversal is : [8, 3, 1, 6, 4, 7, 10, 14, 13]
its in-order traversal is : [1, 3, 4, 6, 7, 8, 10, 13, 14]
Let's see how we reconstruct a tree from its preorder traversal.

preorder[0] = 8 undoubtedly will be the root node.
preorder[1] = 3 might be the left or the right branch of the root node.
From the picture above, 3 must be the left branch of the root node. But how can we know this fact? If we take a look in the in-order traversal, number 3 is on the left of number 8.
So, if we know the position of the numbers in in-order traversal, we can conclude on which side, 2 nodes are located relatively.
inorder[] = [1, 3, 4, 6, 7, 8, 10, 13, 14]
			 |  |  |  |  |  |  |   |   |
position  =  0, 1, 2, 3, 4, 5, 6,  7,  8
preorder[2] = 1: pos[1] < pos[3] < pos[8], number 1 is the left branch of 3, but not the left branch of 8, because the left branch of 8 is already 3. We can conclude:
if ( pos(preorder[i]) < pos(preorder[i-1]) ) then preorder[i] will be the left branch of node preorder[i-1]. Remember, we are reconstruct from the pre-order traversal, it means we go to the most left, then to the right. It means all the previous lefts have already been the left branch of some previous nodes.

preorder[3] = 6: pos[1] < pos[3] < pos[6] < pos[8]
6 must be on the left of 8, but cannot be the left branch of 8, because 3 is already the left branch of 8
6 must be on the right of 3 and 1.
6 cannot be the right branch of 1, because if so, 6 will be on the left side of 3
Therefore, 6 must be the right branch of 3. However, it's still not easy to recognize the pattern to determine if preorder[i] is on the right branch of some node.
So far, we have processed: [8, 3, 1, 6]
6 is on the right branch of 3, so all left branches coming from 3, we no longer have to take care. The list will become **[8,6]

preorder[4] = 4: it's easy, because pos[4] < pos[6], so 4 will be the left branch of 6.
So far, the list needs to process: [8, 6, 4]

preorder[5] = 7: recognize that pos[4] < pos[6] < pos[7] < pos[8]
number 7 will be on the right branch of 6, so all left branches coming from 6, we no longer have to take care. The list will become [8, 7]

Time: O(N)
Space: O(N)
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx = dict()
        for i, val in enumerate(inorder):
            idx[val] = i
        
        stack = []
        head = None
        for val in preorder:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] < idx[stack[-1].val]:
                    stack[-1].left = node
                else:
                    while stack and idx[stack[-1].val] < idx[val]:
                        u = stack.pop()
                    u.right = node
                stack.append(node)
        return head

