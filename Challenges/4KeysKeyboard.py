"""
4 Keys Keyboard

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.
"""

"""
DP
Time: O(N^2)
Space: O(N)

[1 move] Add one A.
[k+1 moves] Multiply the number of A's by K
Say best[k] is the maximum number of A's that can be printed after k moves. The last (simplified) operation must have been addition or multiplication. Thus, best[k] = max(best[k-1] + 1, best[k-2] * 1, best[k-3] * 2, best[k-4] * 3, ...).
"""
class Solution:
    def maxA(self, N: int) -> int:
        dp = [0]*(N+1)
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + 1
            for j in range(i-1):
                dp[i] = max(dp[i], dp[j]*(i - j - 1))
        return dp[-1]

