"""
Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 

Note:

cells.length == 8
cells[i] is in {0, 1}
1 <= N <= 10^9


"""
"""
Approach 1: Simulation
Intuition

We simulate each day of the prison.

Because there are at most 256 possible states for the prison, eventually the states repeat into a cycle rather quickly. We can keep track of when the states repeat to find the period t of this cycle, and skip days in multiples of t.

Algorithm

Let's do a naive simulation, iterating one day at a time. For each day, we will decrement N, the number of days remaining, and transform the state of the prison forward (state -> nextDay(state)).

If we reach a state we have seen before, we know how many days ago it occurred, say t. Then, because of this cycle, we can do N %= t. This ensures that our algorithm only needs O(2∗∗cells.length) steps.
"""
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        
        def update(cells):
            for idx, n in enumerate(cells):
                if idx == 0 or idx == len(cells)-1:
                    cells[idx] = 0
                else:
                    if prev == cells[idx+1]:
                        cells[idx] = 1
                    else:
                        cells[idx] = 0
                prev = n
            return cells
        
        seen=dict()
        while N > 0:
            curr = tuple(cells)
            if curr in seen:
                N %= seen[curr] - N # find the cycle
            seen[curr] = N
            
            if N >= 1:
                N -= 1
                cells = update(cells)
        return cells

