"""
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
"""
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        """
        Use dp to store the result when Alice has x points.
        
        Let f(x) be the answer when we already have x points. When she has between K and N points, then she stops drawing and wins. If she has more than N points, then she loses.

        The key recursion is f(x) = (1/W) * (f(x+1) + f(x+2) + ... + f(x+W))
        This is because there is a probability of 1/W to draw each card from 1 to W.
        
        he difference is f(x) - f(x-1) = 1/W(f(x+W) - f(x)). This allows us to calculate subsequent             f(k)f(k)'s in O(1)O(1) time, by maintaining the numerator S=f(x+1)+f(x+2)+⋯+f(x+W).

        As we calculate each dp[k] = S / W, we maintain the correct value of this numerator S => S + f(k) - f(k+W)S⇒S+f(k)−f(k+W).
        """
        dp = [0.0] * (N+W+1)
        for i in range(K, N+1):
            dp[i] = 1.0
        
        curr = min(N-K+1, W)
        for k in range(K-1, -1, -1):
            dp[k] = curr/W
            curr += dp[k] - dp[k+W]
        return dp[0]
        
        
