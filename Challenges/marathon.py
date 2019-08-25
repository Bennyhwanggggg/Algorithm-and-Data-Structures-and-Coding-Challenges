"""
n students [0, ..., n-1] participate in a marathon. You are given an int array standings where standings[i] = j means that student j finished just before student i. standings[k] = -1 means that k is the first student. There are no ties. List out the students in the order in which they finished the marathon.

Example:

Input: [-1, 0, 1]
Output: [0, 1, 2]
Follow-up:
There are ties.

Example:

Input: [-1, 0, 0]
Output: [0, 1, 2]
"""

def marathon(standings):
	mapping = dict()
	for idx, val in enumerate(standings):
		mapping[val] = idx

	res = []
	person = -1
	while person in standings:
		res.append(mapping[person])
		person = mapping[person]
	return res

def marathon_followup(standings): # change to bfs
	import collections
	graph = collections.defaultdict(list)
	for idx, val in enumerate(standings):
		graph[val].append(idx)

	queue = collections.deque([-1])
	res = []
	while queue:
		curr = queue.popleft()
		for nei in graph[curr]:
			res.append(nei)
			queue.append(nei)
	return res

if __name__ == '__main__':
	assert marathon([-1, 0, 1]) == [0, 1, 2]
	assert marathon_followup([-1, 0, 0]) == [0, 1, 2]