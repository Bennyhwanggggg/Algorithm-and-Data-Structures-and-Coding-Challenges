"""
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]
 

Note:

1 <= N <= 1000
"""
"""
Divide And Conquer


Approach 1: Divide and Conquer
Intuition

This answer is quite unintuitive.

First, notice that the condition is equivalent to saying that A has no arithmetic subsequence. We'll use the term "arithmetic-free" interchangeably with "beautiful".

One way is to guess that we should divide and conquer. One reason for this is that the condition is linear, so if the condition is satisfied by variables taking on values (1, 2, ..., n), it is satisfied by those variables taking on values (a + b, a + 2*b, a + 3*b, ..., a + (n-1)*b) instead.

If we perform a divide and conquer, then we have two parts left and right, such that each part is arithmetic-free, and we only want that a triple from both parts is not arithmetic. Looking at the conditions:

2*A[k] = A[i] + A[j]
(i < k < j), i from left, j from right
we can guess that because the left hand side 2*A[k] is even, we can choose left to have all odd elements, and right to have all even elements.

Another way we could arrive at this is to try to place a number in the middle, like 5. We will have 4 and 6 say, to the left of 5, and 7 to the right of 6, etc. We see that in general, odd numbers move towards one direction and even numbers towards another direction.

One final way we could arrive at this is to inspect possible answers arrived at by brute force. On experimentation, we see that many answers have all the odd elements to one side, and all the even elements to the other side, with only minor variation.

Algorithm

Looking at the elements 1, 2, ..., N, there are (N+1) / 2 odd numbers and N / 2 even numbers.

We solve for elements 1, 2, ..., (N+1) / 2 and map these numbers onto 1, 3, 5, .... Similarly, we solve for elements 1, 2, ..., N/2 and map these numbers onto 2, 4, 6, ....

We can compose these solutions by concatenating them, since an arithmetic sequence never starts and ends with elements of different parity.

We memoize the result to arrive at the answer quicker.

Time Complexity: (NlogN). The function f is called only O(logN) times, and each time does O(N) work.

Space Complexity: O(NlogN). 

####

One way is to divide into [1, N / 2] and [N / 2 + 1, N].
But it will cause problems when we merge them.

Another way is to divide into odds part and evens part.
So there is no k with A[k] * 2 = odd + even

I brute force all permutations when N = 5:
20 beautiful array found,
only 4 don't fit odd + even pattern:
[2, 1, 4, 5, 3]
[3, 1, 2, 5, 4]
[3, 5, 4, 1, 2]
[4, 5, 2, 1, 3]


Beautiful Array Properties
Saying that an array is beautiful,
there is no i < k < j,
such that A[k] * 2 = A[i] + A[j]

Apply these 3 following changes a beautiful array,
we can get a new beautiful array


1. Deletion
Easy to prove.

2. Addition
If we have A[k] * 2 != A[i] + A[j],
(A[k] + x) * 2 = A[k] * 2 + 2x != A[i] + A[j] + 2x = (A[i] + x) + (A[j] + x)

E.g: [1,3,2] + 1 = [2,4,3].

3. Multiplication
If we have A[k] * 2 != A[i] + A[j],
for any x != 0,
(A[k] * x) * 2 = A[k] * 2 * x != (A[i] + A[j]) * x = (A[i] * x) + (A[j] * x)

E.g: [1,3,2] * 2 = [2,6,4]


Explanation
With the observations above, we can easily construct any beautiful array.
Assume we have a beautiful array A with length N

A1 = A * 2 - 1 is beautiful with only odds from 1 to N * 2 -1
A2 = A * 2 is beautiful with only even from 2 to N * 2
B = A1 + A2 beautiful array with length N * 2

E.g:

A = [2, 1, 4, 5, 3]
A1 = [3, 1, 7, 9, 5]
A2 = [4, 2, 8, 10, 6]
B = A1 + A2 = [3, 1, 7, 9, 5, 4, 2, 8, 10, 6]

Time Complexity:
I have iteration version here O(N)
Naive recursion is O(NlogN)

For those who may have question about why this method work, I want to share some of my understanding here:

First: divide and conquer, why to divide to odd and even part (or merge odd and even part together)?

that’s say, we have two part: odd = {1, 5, 3}, even = {2, 4, 6}

any number from odd part and any number from even part will alway obey the rule A[k] * 2 != A[i] + A[j]

Ex: 5 from odd part, 6 from even part, for any k between 5 and 6, A[k] * 2 != 5 + 6

So merge two parts will form beautiful array!


Next, we need to make sure the odd and even part are beautiful arrays!

Second: how to find beautiful array that contains only odd (even) number?

as the beautiful array properties that Lee mentioned, Addition and Multiplication

We can get the odd/even beautiful array from previous beautiful array by addition and multiplication

Following is the flow that generate odd and even separately

odd (n * 2 - 1)  	even (n * 2)
1 (1*2-1)	 	2 (1*2)
1 3(2*2-1)  		2 4(2*2)
1 3 5(3*2-1)  	        2 4 6(3*2)


"""
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        memo = {1: [1]}
        
        def f(N):
            if N not in memo:
                odds = f((N+1)//2)
                evens = f(N//2)
                memo[N] = [2*x-1 for x in odds] + [2*x for x in evens]
            return memo[N]
        
        return f(N)

