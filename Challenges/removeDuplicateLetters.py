"""
Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
"""

"""
Greedy with Stack

We will keep a stack to store the solution we have built as we iterate over the string, and we will delete characters off the stack whenever it is possible and it makes our string smaller.

Each iteration we add the current character to the solution if it hasn't already been used. We try to remove as many characters as possible off the top of the stack, and then add the current character

The conditions for deletion are:

The character is greater than the current characters
The character can be removed because it occurs later on
At each stage in our iteration through the string, we greedily keep what's on the stack as small as possible.

Time: O(N)
Space: O(1) as we only keep unique characters
"""
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        last = {val: i for i, val in enumerate(s)}
        
        for i, c in enumerate(s):
            # we can only try to add c if it's not already in our solution
            # this is to maintain only one of each character
            if c not in seen:
                # if the last letter in our solution:
                #    1. exists
                #    2. is greater than c so removing it will make the string smaller
                #    3. it's not the last occurrence (the character in stack can be removed as it has another occurrence later on)
                # we remove it from the solution to keep the solution optimal
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.discard(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)
                    
        

