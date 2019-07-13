"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called. 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time: hasnext: O(1)
      next: O(N)
Space: O(h), for stack

Controlled recursion or do an inoder traversal then use pointer with array

Controlled recursion uses less space

1. Initialize an empty stack S which will be used to simulate the inorder traversal for our binary search tree. Note that we will be following the same approach for inorder traversal as before except that now we will be using our own stack rather than the system stack. Since we are using a custom data structure, we can pause and resume the recursion at will.

2. consider a helper function that we will be calling again and again in the implementation. This function, called _inorder_left will essentially add all the nodes in the leftmost branch of the tree rooted at the given node root to the stack and it will keep on doing so until there is no left child of the root node.

For a given node root, the next smallest element will always be the leftmost element in its tree. So, for a given root node, we keep on following the leftmost branch until we reach a node which doesn't have a left child and that will be the next smallest element. For the root of our BST, this leftmost node would be the smallest node in the tree. Rest of the nodes are added to the stack because they are pending processing. Try and relate this with a dry run of a simple recursive inorder traversal and things will make a bit more sense.

3. The first time next() function call is made, the smallest element of the BST has to be returned and then our simulated recursion has to move one step forward i.e. move onto the next smallest element in the BST. The invariant that will be maintained in this algorithm is that the stack top always contains the element to be returned for the next() function call. However, there is additional work that needs to be done to maintain that invariant. It's very easy to implement the hasNext() function since all we need to check is if the stack is empty or not. So, we will only focus on the next() call from now.

4. When a next() function is called, move back up one stack and check all of its right node's left child and add them to stack
"""
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._leftmost_inorder(root)
        
    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left
        
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        top = self.stack.pop()
        if top.right:
            self._leftmost_inorder(top.right)
        return top.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curr = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack or self.curr else False

    def next(self):
        """
        :rtype: int
        """
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        val = self.curr.val
        self.curr = self.curr.right
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
