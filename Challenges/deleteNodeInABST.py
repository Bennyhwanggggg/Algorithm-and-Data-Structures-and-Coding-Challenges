"""
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Intuition

There are three possible situations here :

Node is a leaf, and one could delete it straightforward : node = null.

Node is not a leaf and has a right child. Then the node could be replaced by its successor which is somewhere lower in the right subtree. Then one could proceed down recursively to delete the successor.

Node is not a leaf, has no right child and has a left child. That means that its successor is somewhere upper in the tree but we don't want to go back. Let's use the predecessor here which is somewhere lower in the left subtree. The node could be replaced by its predecessor and then one could proceed down recursively to delete the predecessor.

Algorithm

If key > root.val then delete the node to delete is in the right subtree root.right = deleteNode(root.right, key).

If key < root.val then delete the node to delete is in the left subtree root.left = deleteNode(root.left, key).

If key == root.val then the node to delete is right here. Let's do it :

If the node is a leaf, the delete process is straightforward : root = null.

If the node is not a leaf and has the right child, then replace the node value by a successor value root.val = successor.val, and then recursively delete the successor in the right subtree root.right = deleteNode(root.right, root.val).

If the node is not a leaf and has only the left child, then replace the node value by a predecessor value root.val = predecessor.val, and then recursively delete the predecessor in the left subtree root.left = deleteNode(root.left, root.val).

Return root.

Time: O(log(N))
SpaceL O(H)
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left or not root.right:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
    
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val


def deleteNode(root, key):
	if not root: # if root doesn't exist, just return it
		return root
	if root.val > key: # if key value is less than root value, find the node in the left subtree
		root.left = deleteNode(root.left, key)
	elif root.val < key: # if key value is greater than root value, find the node in right subtree
		root.right= deleteNode(root.right, key)
	else: #if we found the node (root.value == key), start to delete it
		if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left
			return root.left
		if not root.left: # if it has no left children, we delete the node then new root would be root.right
			return root.right
               # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
		temp = root.right
		mini = temp.val
		while temp.left:
			temp = temp.left
			mini = temp.val
		root.val = mini # replace value
		root.right = deleteNode(root.right,root.val) # delete the minimum node in right subtree
	return root
