"""
Given 2 binary trees root1 and root2. Consider all the leaves of a binary tree. From left to right order, the values of those leaves form a leaf value sequence. For example

	  "x"
	 /   \
 "abc"   "m"
        /   \
     "de"   "y"
            /
          "f"
in the given tree above, the leaf value sequence is (a, b, c, d, e, f).

Two binary trees are considered leaf-similar if their leaf value sequence is the same. Return true if and only if the two given trees are leaf-similar.

Example 1:

Input:
	root1
	 "xyz"
	 /   \
 "abcd"  "aabc"

	root2
	  "xy"
	 /   \
 "abc"  "daabc"

Output: true
Exlanation: "abcd" + "aabc" = "abc" + "daabc"
Example 2:

Input:
	root1
	 "xyz"
	 /   \
 "abcd"  "aabc"

	root2
	  "xy"
	 /   \
 "abc"  "aabc"

Output: false
Exlanation: "abcd" + "aabc" != "abc" + "aabc"
Expected O(1) space solution (recursion stack does count as additional space). Tree node structure is up to you.

class TreeNode {
	String val;
	TreeNode left;
	TreeNode right;
	// add whatever fields you need
}
"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def leafSimilar(rootA, rootB):
	if not rootA or not rootB:
		return False 
	a = getLeafSequence(rootA, '')
	b = getLeafSequence(rootB, '')
	return a == b


def getLeafSequence(root, curr):
	if not root.left and not root.right:
		curr += root.val
		return curr
	leftRes = getLeafSequence(root.left, curr) if root.left else ''
	rightRes = getLeafSequence(root.right, curr) if root.right else ''
	return leftRes + rightRes

if __name__ == '__main__':
	rootA = TreeNode('xyz')
	rootA.left = TreeNode('abcd')
	rootA.right = TreeNode('aabc')
	rootB = TreeNode('xy')
	rootB.left = TreeNode('abc')
	rootB.right = TreeNode('daabc')
	assert leafSimilar(rootA, rootB) == True

	rootA = TreeNode('xyz')
	rootA.left = TreeNode('abcd')
	rootA.right = TreeNode('aabc')
	rootB = TreeNode('xy')
	rootB.left = TreeNode('abc')
	rootB.right = TreeNode('aabc')
	assert leafSimilar(rootA, rootB) == False

	rootA = TreeNode('x')
	rootA.left = TreeNode('abc')
	rootA.right = TreeNode('m')
	rootA.right.left = TreeNode('de')
	rootA.right.right = TreeNode('y')
	rootA.right.right.left = TreeNode('f')
	rootB = TreeNode('xy')
	rootB.left = TreeNode('ac')
	rootB.left.left = TreeNode('a')
	rootB.left.right = TreeNode('bc')
	rootB.right = TreeNode('ax')
	rootB.right.left = TreeNode('de')
	rootB.right.right = TreeNode('f')
	assert leafSimilar(rootA, rootB) == True



