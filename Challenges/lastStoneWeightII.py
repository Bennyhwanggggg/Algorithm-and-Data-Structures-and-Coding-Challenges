"""
Last Stone Weight

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose any two rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the smallest possible weight of this stone (the weight is 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0 so the array converts to [1] then that's the optimal value.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 100
"""

"""
Backtracking

Time: O(2^N)
Space: O(n)
"""
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        mem = {} #Mem
        
        def explore(a, b, stones):
            if len(stones) == 0:
                return abs(a-b)
            
            entry = (a, b, len(stones)) #Mem
            if entry in mem:
                return mem[entry]
            
            s = stones.pop()
            m = min(explore(a+s, b, stones), explore(a, b+s, stones))
            stones.append(s)
            
            mem[entry] = m #Mem
            return m
        
        return explore(0, 0, stones)

"""
DP


Divide the stones into two groups such that the difference of the sum of weights of each group is minimum.

For the problem at the description:
[2,7,4,1,8,1]
Those groups could be:
1,1,2,7 (sum is 11) --- 4,8 (sum is 12)
Difference: 1

Using DP you can check all possible sums of a group.
When you have the sum for one group (e.g.: [4,8] -> 12), you can just subtract that value from the total sum to obtain the sum of the other group.
From the example above. Total sum is 23, the sum for [4,8] is 12, then the sum for the other group is 23-12 = 11. And 12-11 = 1;

So, notice that, if aSum is the sum of a group, the difference of the sums of each group is: Math.abs(totalSum - aSum - aSum).
For this reason you are going to see some solutions doing Math.abs(totalSum - (aSum*2)), which is not that obvious.
So, for each possible 'aSum', minimumAnswer = Math.min(minimumAnswer , Math.abs(totalSum - aSum - aSum));


Suppose you have rock a, b, c and d.
If you subtract them in the following order: b-c, then d-b-c. Then it is the same as doing d-(b+c).
Then doing [d-(b+c)]-a is the same as -a+d-(b+c), which is d-a-(b+c), which is d-[a+(b+c)], which is d-(a+b+c). (So doing things in that order will lead to this shortcut).

Lets try another order.
Suppose you have rock a, b, c and d.
If you do a-d, then b-c, then (a-d)-(b-c).
Then (a-d)-(b-c) is the same as a-d-b+c, which is the same as -d-b+a+c, which is -(d+b)+(a+c), which is (a+c)-(d+b). Another shortcut.

Then you can see that depending on the order of the subtractions, we get a different setting of difference between two groups.
I reiterate that I was not able to come up with that strategy. I just failed the question, then read the most voted answers and spent an hour or so trying to make a sense out of it. Working out these cases seemed to convince me that it works.
"""


"""
we could split the stones into two piles A and B, so that abs( A - B ) has a minimum value. Thus each stone is either in pile A or pile B. now we simply need to figure out how to spilt the stones.
as metioned above, each stone is only in one of the two piles, let's denote dp[i] as whether to put the i-th(starting from 0) stone in to A or B.

if we put it into A, then for all the results that before the i-th stone, we add the weight of i-th stone to them.
if we put it into B, then for all the results that before the i-th stone, we subtract the weight of i-th stone from them.
keep doing this until we put the last stone into calculation. at this point, we simply take a look at final results and the minimum abs value is the answer. below is the code
"""
class Solution:
    def lastStoneWeightII(self, stones) -> int:
        dp = [[]]
        dp[0] = [stones[0],stones[0] * (-1)]
        for i in range(1,len(stones)):
            dp.append([e + stones[i] for e in dp[i - 1]] + [e - stones[i] for e in dp[i - 1]])
            dp[i] = list(set(dp[i]))
        total = list(set(abs(e) for e in dp[-1]))
        total.sort()
        return total[0]
