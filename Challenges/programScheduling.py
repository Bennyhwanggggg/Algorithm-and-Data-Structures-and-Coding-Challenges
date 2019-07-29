"""
Given a sorted list of already scheduled programs and a list of new programs, write an algorithm to find if the given new programs can be scheduled or not? Each program is a pair of values where 1st value is the starting time and 2nd is the execution time.

Example 1:

Input: scheduled = [P1(10, 5), P2(25, 15)], newPrograms = [P3(18, 7), P4(12, 10)]
Output: [true, false]
Explanation: P3(18, 7) starts at time 18 and executes for 7 mins i.e., the end time is 18 + 7 = 25.
So this time slot is free and there is no overlap with already scheduled programs. Hence P3 can be scheduled. 
As the P4 overlaps with P1, so P4 cannot be scheduled.
Example 2:

Input: scheduled = [P1(10, 5), P2(25, 15)], newPrograms = [P3(18, 7), P4(20, 2)]
Output: [true, false]
Explanation: P3 can be scheduled so we add it to already scheduled programs. P4 overlaps with P3, so P4 cannot be scheduled.
"""

"""
Time: O(n^2)
Space: O(n)
"""
def programScheduling(scheduled, newPrograms):
	res = []
	for newProgram in newPrograms:
		if not len(scheduled) or (newProgram[0] >= scheduled[len(scheduled)-1][0]+scheduled[len(scheduled)-1][1]): # check if it can be a new last program
			scheduled.append(newProgram)
			res.append(True)
		else:
			for i in range(len(scheduled)):
				if newProgram[0]+newProgram[1] <= scheduled[i][0]: # new program is totally before the current scheduled node, insert it
					scheduled.insert(i, newProgram)
					res.append(True)
					break
				elif max(newProgram[0], scheduled[i][0]) < min(newProgram[0]+newProgram[1], scheduled[i][0]+scheduled[i][1]):
					res.append(False)
					break
	return res

if __name__ == '__main__':
	assert programScheduling([], [(18, 7), (29, 10)]) == [True, True]
	assert programScheduling([(10, 5), (25, 15)], [(18, 7), (12, 10)]) == [True, False]
	assert programScheduling([(10, 5), (25, 15)], [(18, 7), (20, 2)]) == [True, False]
	assert programScheduling([(10, 1000)], [(18, 7), (12, 10)]) == [False, False]
	assert programScheduling([(1,1), (3,1)], [(2,1), (4,1)]) == [True, True]