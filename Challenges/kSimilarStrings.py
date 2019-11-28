"""
K Similar Strings

Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}

"""

"""
We can treat each string as a node. If two strings x and y differ by one swap and that swap makes x more simliar to target string B, there is a directed edges between them.
So we can build a directed graph BFS based on that to find the value of k.

I used a function nei to generate all children node of a node x. Each child node requires one swap to change from x and each child node has one character more similiar to B than x.

Then we just perform a regular BFS. Since A and B are garuanteed to be k-similiar. We can always reach B from A.

Time: O(N^3)
"""
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def nei(x):
            i = 0
            while x[i] == B[i]:
                i+=1
            for j in range(i+1, len(x)):
                if x[j] == B[i]: 
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
                
        q, seen = [(A,0)], {A}
        for x, d in q:
            if x == B:
                return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y), 
                    q.append((y,d+1))

