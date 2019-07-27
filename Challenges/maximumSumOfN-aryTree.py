"""
Given an N-ary tree and the weight of each edge represented in the value at the child node, now we are pouring water from root node and it gradually coming down through each node traversing one by one. Now time taken by the water to come from parent to child node was written by the value at child node and also root.value = 0 as time taken by root to get wet is 0 sec. Now you need to find the total time required by all nodes to get wet.

Example

				   0
		3.     2.     4
	5		6

We are pouring water from root node-
1)Time required to go to 1st child is 3
2)Time required to go to 2nd child is 2
3)Time required to go to 3rd child is 4
4)Time required to go to 1st child of node "3" is 5+3=8
5)Time required to go to 2nd child of node "3" is 3+6=9
So total time required by all node to get wet is 9.
"""
import collections

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.children = None

def water_tower(root):
	queue = collections.deque([(node, 0) for node in root.children])
	max_sum = 0

	while queue:
		node, curr_sum = queue.popleft()
		curr_sum += node.val
		max_sum = max(max_sum, curr_sum)
		if not node.children:
			continue
		for child in node.children:
			queue.append((child, curr_sum))

	return max_sum


if __name__ == '__main__':
	left = TreeNode(3)
	left.children = [TreeNode(5), TreeNode(6)]
	center = TreeNode(2)
	right = TreeNode(4)
	root = TreeNode(0)
	root.children = [left, center, right]

	assert water_tower(root) == 9

