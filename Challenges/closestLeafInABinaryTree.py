"""
Closest Leaf in a Binary Tree

Given a binary tree where every node has a unique value, and a target key k, find the value of the nearest leaf node to target k in the tree.

Here, nearest to a leaf means the least number of edges travelled on the binary tree to reach any leaf of the tree. Also, a node is called a leaf if it has no children.

In the following examples, the input tree is represented in flattened form row by row. The actual root tree given will be a TreeNode object.

Example 1:

Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)

Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.
Example 2:

Input:
root = [1], k = 1
Output: 1

Explanation: The nearest leaf node is the root node itself.
Example 3:

Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation: The leaf node with value 3 (and not the leaf node with value 6) is nearest to the node with value 2.
Note:
root represents a binary tree with at least 1 node and at most 1000 nodes.
Every node has a unique node.val in range [1, 1000].
There exists some node in the given binary tree for which node.val == k.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Intuition

Instead of a binary tree, if we converted the tree to a general graph, we could find the shortest path to a leaf using breadth-first search.

Algorithm

We use a depth-first search to record in our graph each edge travelled from parent to node.

After, we use a breadth-first search on nodes that started with a value of k, so that we are visiting nodes in order of their distance to k. When the node is a leaf (it has one outgoing edge, where the root has a "ghost" edge to null), it must be the answer.

Time: O(N)
Space: O(N)
"""
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        
        def dfs(node, parent=None):
            if node:
                graph[node].append(parent)
                graph[parent].append(node)
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = collections.deque(node for node in graph if node and node.val == k)
        seen = set(queue)
        while queue:
            node = queue.popleft()
            if not node:
                continue
            if len(graph[node]) <= 1:
                return node.val
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        graph = collections.defaultdict(list)
        
        def dfs(node, parent=None):
            if not node:
                return
            graph[node].append(parent)
            graph[parent].append(node)
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root)
        seen = set()
        queue = collections.deque([node for node in graph if node and node.val == k])
        while queue:
            node = queue.popleft()
            seen.add(node)
            if not node:
                continue
            if len(graph[node]) <= 1:
                return node.val
            for nei in graph[node]:
                if nei not in seen:
                    queue.append(nei)                

