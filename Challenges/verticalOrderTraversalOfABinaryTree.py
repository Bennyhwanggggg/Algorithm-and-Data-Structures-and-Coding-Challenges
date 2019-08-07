"""
Vertical Order Traversal of a Binary Tree

Given a binary tree, return the vertical order traversal of its nodes values.

For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.

 

Example 1:



Input: [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation: 
Without loss of generality, we can assume the root node is at position (0, 0):
Then, the node with value 9 occurs at position (-1, -1);
The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
The node with value 20 occurs at position (1, -1);
The node with value 7 occurs at position (2, -2).
Example 2:



Input: [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]
Explanation: 
The node with value 5 and the node with value 6 have the same position according to the given scheme.
However, in the report "[1,5,6]", the node value of 5 comes first since 5 is smaller than 6.
 

Note:

The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Store locations

Intuition

It's evident that there are two steps in a straightforward solution: first, find the location of every node, then report their locations.

Algorithm

To find the location of every node, we can use a depth-first search. During the search, we will maintain the location (x, y) of the node. As we move from parent to child, the location changes to (x-1, y+1) or (x+1, y+1) depending on if it is a left child or right child. [We use y+1 to make our sorting by decreasing y easier.]

To report the locations, we sort them by x coordinate, then y coordinate, so that they are in the correct order to be added to our answer.


->Root node is considered as 0 horizontal distance.
->As we move left hd is decreased by 1 and is increased by 1 as we move right.
->vd is used to get the top to bottom series.
->comparison in each dic is done based on vd value
-> if vd comes out to be same then node value is compared.

Time: O(Nlog(N))
Space: O(N)
"""
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        graph = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        ans=[]
        while queue:
            temp = collections.deque()
            while queue:
                node, hd, vd = queue.popleft()
                graph[hd].append((vd, node.val))
                if node.left:
                    temp.append((node.left, hd-1, vd-1))
                if node.right:
                    temp.append((node.right, hd+1, vd-1))
            queue = temp
        
        for i in sorted(graph.keys()):
            level = [x[1] for x in sorted(graph[i], key=lambda x:(-x[0], x[1]))]   
            ans.append(level)
        return ans

