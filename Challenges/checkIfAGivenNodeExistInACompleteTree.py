"""
Given a complete(virtual) binary tree, return true/false if the given target node exists in the tree or not.
Here, the "virtual" means the tree nodes are numbered assuming the tree is a complete binary tree.

For example:

                1
		    /        \ 
		 2              3
       /   \           /  \ 
     4   (5)nil      6  (7)nil
   
   //function signature
   // bool doesNodeExist(root *TreeNode, target int)
   doesNodeExist(root, 4) -> true
   doesNodeExist(root, 7) -> false, Given the node on #7 is a nil node.
   
   //Level order traversal solution, numbering the left(2n+1) and right(2n+2) children node is a trivial solution(time O(n)/O(target) and space O(n)/O(target)). 
   //Think of a better solution.
"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


def doesNodeExist(root, target):
	if not root:
		return False 

	path = getPathFromRootTo(target)
	return verifyPath(root, path)


def getPathFromRootTo(child):
	stack = []
	while child != 1:
		stack.append(child)
		child = getParentIndex(child)

	return stack


def getParentIndex(childIndex):
	return childIndex//2;


def verifyPath(node, path):
	while path:
		val = path.pop()
		node = node.left if val%2 == 0 else node.right
		if not node:
			return False
	return True

if __name__ == '__main__':
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.left.left = TreeNode(4)
	root.right = TreeNode(3)
	root.right.left = TreeNode(6)
	assert doesNodeExist(root, 5) == False
	assert doesNodeExist(root, 7) == False
	assert doesNodeExist(root, 20) == False
	assert doesNodeExist(None, 1) == False
	assert doesNodeExist(root, 1) == True
	assert doesNodeExist(root, 2) == True
	assert doesNodeExist(root, 3) == True
	assert doesNodeExist(root, 4) == True
	assert doesNodeExist(root, 6) == True

