"""
Find all the nodes that can enter a cycle in a graph
"""
import defaultdict

"""
Find all the nodes that can enter a cycle in a graph. Is the graph directed or undirected? Can the graph have multiple cycles? Can it have multiple connected components? Here's what I'm thinking:

In a connected component, start DFS from any point and the moment you visit some already visited point, mark that point as start for step 2.
Start from previously marked point and perform DFS. Maintain a set of Nodes that are visited in the DFS path (this is apart from the visited set across all paths). The path where we end up visiting the start again, will have the set of nodes in the cycle.
"""
def findNodesCycle(nV, edges):
	seen = set()
	saw = set()
	cycles = []
	graph = collections.defaultdict(list)
	for a, b in edges:
		graph[a].append(b)


	def dfs(node):
		if node in saw:
			return False
		if node in seen:
			return True
		saw.add(node)
		for nei in graph[node]:
			if not dfs(nei):
				return False
		saw.remove(node)
		seen.add(node)
		return True 

	for i in range(nV):
		if not dfs(i):
			cycles.append(i)

	return cucles