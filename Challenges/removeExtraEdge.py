"""
Given a binary tree, where an arbitary node has 2 parents i.e two nodes in the tree have the same child. Identify the defective node and remove an extra edge to fix the tree.

Example:

Input:
	   1
	  / \
	 2   3
	/ \ /
   4   5

Output:

     1			       1
    / \			      / \
   2   3    or	     2   3
  / \ 			    /   /
 4   5		       4   5

Explanation: We can remove either 3-5 or 2-5.
Solution
Follow-up 1:
What if the tree is a BST?

Example:

Input:
       3
	  / \
	 2   5
	/ \ /
   1   4

Output:
       3
	  / \
	 2   5
	/   /
   1   4

Explanation: In this case we can only remove 2-4 because if we remove 5-4 the BST will be invalid.
"""
class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


def removeExtraEdge(root):
	if not root:
		return root

	def helper(node, seen):
		if not node or node in seen:
			return None
		seen.add(node)
		node.left = helper(node.left, seen)
		node.right = helper(node.right, seen)
		return node

	seen = set()
	return helper(node, seen)

def removeExtraEdgeBST(root):

	def helper(node, left, right):
		if not node:
			return node
		if left >= node.val or right <= node.val:
			return None
		node.left = helper(node.left, left, node.val)
		node.right = helper(node.right, node.val, right)
		return node
	return helper(root, -float('inf'), float('inf'))


