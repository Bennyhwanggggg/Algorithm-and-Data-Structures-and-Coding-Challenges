"""
Campus Bikes II

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.
"""

"""
At first I implemented the solution with backtracking, but with this approach you need to generate all possible assignments which has factorial complexity. I was passing over the bikes that were not assigned yet (left_bikes) and the current worker I was assigning a bike to, and effectively in this situation we have repeated calls:

I assign the first bike to the first worker, and then I assign the second bike to the second worker, my current worker will be 3 and my left bikes will be all but first and second. On a different branch I assign the first bike to the second worker, and then the second bike to the first worker, and I have the same as before, current worker 3 and left bikes all but first and second.

The thing is, I cannot memorize with this approach, because the assignments are different, so I cannot use the information from the past branch to get the distance on this different branch, then I will get time limit.

Clearly, the way to go is dynamic programming, if I build a bottom up solution then I can use the information from the past seen calls into my current assignment:

left_bikes is an array the size of bikes, which has a 0 if bike[i] has been assigned or not. You can generate a new array on every call or pass it by reference and update it in a backatracking fashion, which I did to save space.
cur_worker is the index of the current worker I need to assign a bike to
In order to memorize, left_bikes need to be transformed into a tuple, since lists are not hashable.
"""
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        
        def assign(left_bikes, curr_worker):
            info = (curr_worker, tuple(left_bikes))  # unique identifier of the call parameters 
            if info in self.seen:   # if I have computed the min distance for this paramenters before
                return self.seen[info]
            if curr_worker == len(workers):  # if I already assigned all workers
                return 0
            temp = float('inf')  # start calculating the minimum from this assignment onwards
            for j in range(len(left_bikes)):
                if left_bikes[j] == 0:
                    left_bikes[j] = 1 # assign all left bikes to the current worker
                    wx, wy = workers[curr_worker] 
                    bx, by = bikes[j]
                    temp = min(temp, abs(wx - bx) + abs(wy - by) + assign(left_bikes, curr_worker + 1)) # update my minimum considering the minimum between what I had and the distance of this assignment + the minimum distance for the future assignments 
                    left_bikes[j] = 0 # unassign bike (instead of creating new left_bike array for every call)
            self.seen[info] = temp # memorize
            return temp 
        
        self.seen = dict()
        return assign([0 for i in range(len(bikes))], 0) # start with all bikes unassigned and with worker 0

