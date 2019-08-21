"""
Task Scheduler
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

"""
To do so, firstly, we put only those elements from map into the queue which have non-zero number of instances. Then, we start picking up the largest task from the queue for current execution. (Again, at every instant, we update the current time as well.) We pop this element from the queue. We also decrement its pending number of instances and if any more instances of the current task are pending, we store them(count) in a temporary temp list, to be added later on back into the queue. We keep on doing so, till a cycle of cooling time has been finished. After every such cycle, we add the generated temp list back to the queue for considering the most critical task again.

We keep on doing so till the queue(and temp) become totally empty. At this instant, the current value of timetime gives the required result.

This is an extremely tricky problem.
The main idea is to schedule the most frequent tasks as frequently as possible. Begin with scheduling the most frequent task. Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.
Exampe: Say we have the following tasks: [A,A,A,B,C,D,E] with n =2
Now if we schedule using the idea of scheduling all unique tasks once and then calculating if a cool-off is required or not, then we have: A,B,C,D,E,A,idle,dile,A i.e. 2 idle slots.
But if we schedule using most frequent first, then we have:
2.1: A,idle,idle,A,idle,idle,A
2.2: A,B,C,A,D,E,A i.e. no idle slots. This is the general intuition of this problem.
3.The idea in two can be implemented using a heap and temp list. This is illustrated in the code below.
4.Time complexity is O(N * n) where N is the number of tasks and n is the cool-off period.
5.Space complexity is O(1) - will not be more than O(26).
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        curr_time, pq = 0, []
        for task, count in collections.Counter(tasks).items():
            heapq.heappush(pq, (-count, task))
            
        while pq:
            i, temp = 0, []
            while i <= n:
                curr_time += 1
                if pq:
                    count, task = heapq.heappop(pq)
                    if count != -1:
                        temp.append((count+1, task))
                if not pq and not temp: # exit when no more task
                    break
                else:
                    i += 1
            for item in temp:
                heapq.heappush(pq, item)
        return curr_time

