"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

 

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
 

Note:

Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.

Solution
Intuition

We only care about the most recent calls in the last 3000 ms, so let's use a data structure that keeps only those.

Algorithm

Keep a queue of the most recent calls in increasing order of t. When we see a new call with time t, remove all calls that occurred before t - 3000.
"""
class RecentCounter:

    def __init__(self):
        """
        self.counter = []
        """
        self.queue = collections.deque()
        
    def ping(self, t: int) -> int:
        """
        Naive timeout solution
        self.counter.append(t)
        count = 0
        for i in self.counter:
            if t - 3000 <= i or t-3000 <= 0:
                count += 1
        return count
        """
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)
