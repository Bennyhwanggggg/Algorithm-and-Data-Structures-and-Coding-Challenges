"""
A binary tree has the binary search tree property (BST property) if, for every node, the keys in its left subtree are smaller than its own key, and the keys in its right subtree are larger than its own key. It has the heap property if, for every node, the keys of its children are all smaller than its own key. You are given a set of binary tree nodes (i, j) where each node contains an integer i and an integer j. No two i values are equal and no two j values are equal. We must assemble the nodes into a single binary tree where the i values obey the BST property and the j values obey the heap property. If you pay attention only to the second key in each node, the tree looks like a heap, and if you pay attention only to the first key in each node, it looks like a binary search tree.

Example 1:

Input: [(1, 6), (3, 7), (2, 4)]
Output:

		(3, 7)
		/
	 (1, 6)
		\
	  (2, 4)
Example 2:

Input: [(1, 4), (8, 5), (3, 6), (10, -1), (4, 7)]
Output:

		(4, 7)
		/    \
	(3, 6)   (8, 5)
	 /          \
 (1, 4)       (10, -1)
You can assume that a solution always exists.
"""

# https://leetcode.com/discuss/interview-question/363945/google-special-binary-tree
class TreeNode:
    def __init__(self, x, y):
        self.left = self.right = None
        self.key1, self.key2 = x, y
        
def checkBST(node):
    if node is None: return True
    l, r = node.left, node.right
    while l and l.right: l = l.right
    while r and r.left: r = r.left
    l_val = l.key1 if l else  -float('inf') 
    r_val = r.key1 if r else  float('inf')
    return l_val < node.key1 < r_val and checkBST(node.left) and checkBST(node.right)
    
def checkHeap(node):
    if node is None: return True, -float('inf')
    chk_l, val_l = checkHeap(node.left)
    chk_r, val_r = checkHeap(node.right)
    chk = node.key2 > max(val_l, val_r) and chk_l and chk_r
    val = max(node.key2, val_l, val_r)
    return chk, val
    
        
def specialBinaryTree(pairs):
    # Sort according to second value
    pairs.sort(key=lambda x: x[1], reverse=True)
    def helper(pairs):
        if not pairs: return None
        # Create root node
        x0, y0 = pairs[0]
        node = TreeNode(x0, y0)
        # Split left and right according to first value
        node.left = helper([(x, y) for x, y in pairs if x < x0])
        node.right = helper([(x, y) for x, y in pairs if x > x0])
        return node
    return helper(pairs)

pairs = [(1, 6), (3, 7), (2, 4)]
root = specialBinaryTree(pairs)
print(checkBST(root), checkHeap(root)[0])

paris = [(1, 4), (8, 5), (3, 6), (10, -1), (4, 7)]
root = specialBinaryTree(pairs)
print(checkBST(root), checkHeap(root)[0])