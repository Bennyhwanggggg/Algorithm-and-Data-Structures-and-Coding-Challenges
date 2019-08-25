"""
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads.

Example 1:

Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.
"""

# maximise one to be the half of total
def solution(processes):
	max_load = sum(processes)
	total = max_load // 2
	dp = [[0 for i in range(len(processes))] for j in range(total)]
	for i in range(1, total + 1):
		if i >= processes[0]:
			dp[i-1][0] = processes[0]

	for idx, item in enumerate(processes):
		for w in range(2, total+1):
			if w-1 < item:
				dp[w-1][idx] = dp[w-1][idx-1]
			else:
				dp[w - 1][idx] = max(dp[w - 1][idx - 1], dp[w - item - 1][idx - 1] + item)

	best = dp[total - 1][len(processes) - 1]
	return  max_load - 2*best