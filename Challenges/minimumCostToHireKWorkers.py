"""
Minimum Cost To Hire K Workers

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""

"""
Optimal: Heap

The major insight that they don't explain clearly is as follows. We want to figure out which worker is the one who is supposed to be paid their minimum wage. We know that at least one person is getting paid minimum wage, and so we want to be able to easily say if we pay one person minimum wage, who are the other people that we can afford.

We do this by computing the ratio of price to quality, or essentially computing the price per unit of quality. Then if we compare the ratios, we know that if we hire a person with ratio X at minimum wage, we can hire anyone with a ratio <= X while paying the person minimum wage.

Why is this the case? We can pretty clearly logic our way through this. If one person charges less for the same amount of quality and we're paying each person relative to their amount of quality, then the person who charges less is happier getting paid relative to the person who charges more. A simple example:

person1: wage = 10, quality = 5, ratio = 10/5 = 2
person2: wage = 5, quality = 10, ratio = 5/10 = 0.5
If we pay person1 their minimum wage, then they earn 10 and person2 earns 20. That's fine. However, if we pay person2 their minimum wage, they earn 5 and person1 only earns 2.5, which is not allowed. Note how the ratios basically reflect this.

So that's how the ratios affect things here. Now how do we use this?

Well as long as we are paying everyone their minimum wage, we know we want to hire the lowest quality people possible. Since we're paying in proportion to quality, the lower quality the people, the cheaper they will be for us to actually hire.

So our basic approach is to say, for each person, assume we're paying them minimum wage and then use the ratios to quickly find everyone we can hire for a rate proportional to their minimum wage. Then of that group of people, find the K-1 people with the lowest quality because that will be the cheapest configuration with that initial person getting their minimum wage.

If you read the code for their solution, they optimize all of this stuff. We use a heap to maintain a set of the K lowest-quality workers that we've seen so far and then we iterate over the workers in order of ratio from lowest to highest.

That means that for each worker in our list, if there are K-1 workers in the heap, we instantly have the K-1 lowest quality workers that we can hire where the current worker can be paid their minimum wage. We're just going to look at each of these combinations.

Finally, they do one more optimization. If you just did what I described, it would take you O(K) to compute the total amount you need to pay each time. However, by tracking the sum of the quality of the K-1 lowest quality workers, you are able to compute the total amount in constant time. Remember that everyone needs to be getting paid the same amount per unit of quality, and we have the ratio that that should be, so we just have to pay maxRatio * totalQuality.

Intuition

A least one worker is paid their minimum wage expectation.

Additionally, every worker has some minimum ratio of dollars to quality that they demand. For example, if wage[0] = 100 and quality[0] = 20, then the ratio for worker 0 is 5.0.

The key insight is to iterate over the ratio. Let's say we hire workers with a ratio R or lower. Then, we would want to know the K workers with the lowest quality, and the sum of that quality. We can use a heap to maintain these variables.

Algorithm

Maintain a max heap of quality. (We're using a minheap, with negative values.) We'll also maintain sumq, the sum of this heap.

For each worker in order of ratio, we know all currently considered workers have lower ratio. (This worker will be the 'captain', as described in Approach #1.) We calculate the candidate answer as this ratio times the sum of the smallest K workers in quality.

Time: O(Nlog(N))
Space: O(N)
"""
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        workers = sorted((w/q, q, w)
                         for q, w in zip(quality, wage))

        ans = float('inf')
        pool = []
        sumq = 0
        for ratio, q, w in workers:
            heapq.heappush(pool, -q)
            sumq += q

            if len(pool) > K:
                sumq += heapq.heappop(pool)

            if len(pool) == K:
                ans = min(ans, ratio * sumq)

        return float(ans)
    
"""
Greedy
Intuition

At least one worker will be paid their minimum wage expectation. If not, we could scale all payments down by some factor and still keep everyone earning more than their wage expectation.

Algorithm

For each captain worker that will be paid their minimum wage expectation, let's calculate the cost of hiring K workers where each point of quality is worth wage[captain] / quality[captain] dollars. With this approach, the remaining implementation is straightforward.

Note that this algorithm would not be efficient enough to pass larger test cases.

Time: O(N^2log(N))
Space: O(N)
"""
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        ans = float('inf')

        N = len(quality)
        for captain in range(N):
            # Must pay at least wage[captain] / quality[captain] per qual
            factor = wage[captain]/quality[captain]
            prices = []
            for worker in range(N):
                price = factor * quality[worker]
                if price < wage[worker]: 
                    continue
                prices.append(price)

            if len(prices) < K: 
                continue
            prices.sort()
            ans = min(ans, sum(prices[:K]))

        return float(ans)   
    

